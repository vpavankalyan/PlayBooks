import logging
from typing import Union

from django.db.models import QuerySet
from django.http import HttpResponse, HttpRequest

from google.protobuf.wrappers_pb2 import BoolValue, StringValue

from accounts.models import Account, get_request_account, get_request_user, get_api_token_user
from executor.crud.playbook_execution_crud import create_playbook_execution, get_db_playbook_execution
from executor.crud.playbooks_crud import create_db_playbook
from executor.crud.playbooks_update_processor import playbooks_update_processor
from executor.task_executor import execute_task
from executor.tasks import execute_playbook
from management.crud.task_crud import get_or_create_task, check_scheduled_or_running_task_run_for_task
from management.models import TaskRun, PeriodicTaskStatus
from playbooks.utils.decorators import api_blocked, web_api, account_post_api, account_get_api
from playbooks.utils.meta import get_meta
from playbooks.utils.queryset import filter_page
from playbooks.utils.utils import current_epoch_timestamp, current_datetime
from protos.base_pb2 import Meta, TimeRange, Message, Page
from protos.playbooks.api_pb2 import RunPlaybookTaskRequest, RunPlaybookTaskResponse, RunPlaybookStepRequest, \
    RunPlaybookStepResponse, CreatePlaybookRequest, CreatePlaybookResponse, GetPlaybooksRequest, GetPlaybooksResponse, \
    UpdatePlaybookRequest, UpdatePlaybookResponse, ExecutePlaybookRequest, ExecutePlaybookResponse, \
    ExecutionPlaybookGetRequest, ExecutionPlaybookGetResponse, ExecutionsPlaybooksListResponse, \
    ExecutionsPlaybooksListRequest, ExecutionPlaybookAPIGetResponse
from protos.playbooks.playbook_pb2 import PlaybookTaskExecutionResult, Playbook as PlaybookProto
from utils.proto_utils import proto_to_dict, dict_to_proto

logger = logging.getLogger(__name__)


@web_api(RunPlaybookTaskRequest)
def task_run(request_message: RunPlaybookTaskRequest) -> Union[RunPlaybookTaskResponse, HttpResponse]:
    account: Account = get_request_account()
    meta: Meta = request_message.meta
    time_range: TimeRange = meta.time_range
    if not time_range.time_lt or not time_range.time_geq:
        current_time = current_epoch_timestamp()
        time_range = TimeRange(time_geq=int(current_time - 14400), time_lt=int(current_time))
    task = request_message.playbook_task_definition
    try:
        task_execution_result = execute_task(account.id, time_range, task)
    except Exception as e:
        return RunPlaybookTaskResponse(meta=get_meta(tr=time_range), success=BoolValue(value=False),
                                       task_execution_result=PlaybookTaskExecutionResult(
                                           error=StringValue(value=str(e))))
    return RunPlaybookTaskResponse(meta=get_meta(tr=time_range), success=BoolValue(value=True),
                                   task_execution_result=task_execution_result)


@web_api(RunPlaybookStepRequest)
def step_run(request_message: RunPlaybookStepRequest) -> Union[RunPlaybookStepResponse, HttpResponse]:
    account: Account = get_request_account()
    step = request_message.playbook_step
    tasks = step.tasks
    task_execution_results = []
    meta: Meta = request_message.meta
    time_range: TimeRange = meta.time_range
    if not time_range.time_lt or not time_range.time_geq:
        current_time = current_epoch_timestamp()
        time_range = TimeRange(time_geq=int(current_time - 14400), time_lt=int(current_time))
    for task in tasks:
        try:
            task_result = execute_task(account.id, time_range, task)
            task_execution_results.append(task_result)
        except Exception as e:
            task_execution_results.append(PlaybookTaskExecutionResult(error=StringValue(value=str(e))))

    return RunPlaybookStepResponse(meta=get_meta(tr=time_range), success=BoolValue(value=True), name=step.name,
                                   description=step.description, task_execution_results=task_execution_results)


@web_api(GetPlaybooksRequest)
def playbooks_get(request_message: GetPlaybooksRequest) -> Union[GetPlaybooksResponse, HttpResponse]:
    account: Account = get_request_account()
    meta: Meta = request_message.meta
    show_inactive = meta.show_inactive
    page: Page = meta.page
    list_all = True

    qs: QuerySet = account.playbook_set.all()
    if request_message.playbook_ids:
        qs = qs.filter(id__in=request_message.playbook_ids)
        list_all = False
    elif not show_inactive or not show_inactive.value:
        qs = qs.filter(is_active=True, is_generated=False)

    total_count = qs.count()
    qs = qs.order_by('-created_at')
    qs = filter_page(qs, page)

    playbooks_list = list(pb.proto_partial for pb in qs)
    if not list_all:
        playbooks_list = list(pb.proto for pb in qs)

    return GetPlaybooksResponse(meta=get_meta(page=page, total_count=total_count), playbooks=playbooks_list)


@api_blocked
@web_api(CreatePlaybookRequest)
def playbooks_create(request_message: CreatePlaybookRequest) -> Union[CreatePlaybookResponse, HttpResponse]:
    account: Account = get_request_account()
    user = get_request_user()
    playbook: PlaybookProto = request_message.playbook
    if not playbook or not playbook.name:
        return CreatePlaybookResponse(success=BoolValue(value=False),
                                      message=Message(title="Invalid Request", description="Missing name/playbook"))
    playbook, error = create_db_playbook(account, user.email, playbook)
    if error:
        return CreatePlaybookResponse(success=BoolValue(value=False), message=Message(title="Error", description=error))
    return CreatePlaybookResponse(success=BoolValue(value=True), playbook=playbook.proto)


@api_blocked
@web_api(UpdatePlaybookRequest)
def playbooks_update(request_message: UpdatePlaybookRequest) -> Union[UpdatePlaybookResponse, HttpResponse]:
    account: Account = get_request_account()
    user = get_request_user()
    playbook_id = request_message.playbook_id.value
    update_playbook_ops = request_message.update_playbook_ops
    if not playbook_id or not update_playbook_ops:
        return UpdatePlaybookResponse(success=BoolValue(value=False),
                                      message=Message(title="Invalid Request", description="Missing playbook_id/ops"))
    try:
        account_playbook = account.playbook_set.get(id=playbook_id)
    except Exception as e:
        logger.error(f"Error fetching playbook: {e}")
        return UpdatePlaybookResponse(success=BoolValue(value=False),
                                      message=Message(title="Error", description=str(e)))
    if account_playbook.created_by != user.email:
        return UpdatePlaybookResponse(success=BoolValue(value=False),
                                      message=Message(title="Invalid Request",
                                                      description="Unauthorized Action for user"))
    try:
        playbooks_update_processor.update(account_playbook, update_playbook_ops)
    except Exception as e:
        logger.error(f"Error updating playbook: {e}")
        return UpdatePlaybookResponse(success=BoolValue(value=False),
                                      message=Message(title="Error", description=str(e)))
    return UpdatePlaybookResponse(success=BoolValue(value=True))


@web_api(ExecutePlaybookRequest)
def playbooks_execute(request_message: ExecutePlaybookRequest) -> Union[ExecutePlaybookResponse, HttpResponse]:
    account: Account = get_request_account()
    user = get_request_user()
    meta: Meta = request_message.meta
    time_range: TimeRange = meta.time_range
    current_time = current_epoch_timestamp()
    if not time_range.time_lt or not time_range.time_geq:
        time_range = TimeRange(time_geq=int(current_time - 14400), time_lt=int(current_time))
    playbook_id = request_message.playbook_id.value
    if not playbook_id:
        return ExecutePlaybookResponse(meta=get_meta(tr=time_range), success=BoolValue(value=False),
                                       message=Message(title="Invalid Request", description="Missing playbook_id"))
    playbook_run_uuid = f'{str(current_time)}_{account.id}_{playbook_id}_pb_run'
    try:
        playbook_execution = create_playbook_execution(account, time_range, playbook_id, playbook_run_uuid, user.email)
    except Exception as e:
        logger.error(e)
        return ExecutePlaybookResponse(success=BoolValue(value=False),
                                       message=Message(title="Error", description=str(e)))

    saved_task = get_or_create_task(execute_playbook.__name__, account.id, playbook_id, playbook_execution.id,
                                    proto_to_dict(time_range))
    if saved_task:
        if not check_scheduled_or_running_task_run_for_task(saved_task):
            current_date_time = current_datetime()
            task = execute_playbook.delay(account.id, playbook_id, playbook_execution.id, proto_to_dict(time_range))
            try:
                saved_task_run = TaskRun.objects.create(task=saved_task, task_uuid=task.id,
                                                        status=PeriodicTaskStatus.SCHEDULED,
                                                        account_id=account.id,
                                                        scheduled_at=current_date_time)
            except Exception as e:
                logger.error(f"Exception occurred while saving task run for account: {account.id}, "
                             f"task: {saved_task.id}, error: {e}")
    else:
        logger.error(f"Failed to create task for playbook execution: {playbook_run_uuid}")
        return ExecutePlaybookResponse(meta=get_meta(tr=time_range), success=BoolValue(value=False),
                                       message=Message(title="Error",
                                                       description="Failed to create task for playbook execution"))

    return ExecutePlaybookResponse(meta=get_meta(tr=time_range), success=BoolValue(value=True),
                                   playbook_run_id=StringValue(value=playbook_run_uuid))


@web_api(ExecutionPlaybookGetRequest)
def playbooks_execution_get(request_message: ExecutionPlaybookGetRequest) -> \
        Union[ExecutionPlaybookGetResponse, HttpResponse]:
    account: Account = get_request_account()
    playbook_run_id = request_message.playbook_run_id.value
    if not playbook_run_id:
        return ExecutionPlaybookGetResponse(success=BoolValue(value=False), message=Message(title="Invalid Request",
                                                                                            description="Missing playbook_run_id"))
    try:
        playbook_execution = get_db_playbook_execution(account, playbook_run_id=playbook_run_id)
        if not playbook_execution:
            return ExecutionPlaybookGetResponse(success=BoolValue(value=False), message=Message(title="Error",
                                                                                                description="Playbook Execution not found"))
    except Exception as e:
        return ExecutionPlaybookGetResponse(success=BoolValue(value=False),
                                            message=Message(title="Error", description=str(e)))

    playbook_execution = playbook_execution.first()
    time_range = playbook_execution.time_range
    time_range_proto = dict_to_proto(time_range, TimeRange) if time_range else TimeRange()
    return ExecutionPlaybookGetResponse(meta=get_meta(time_range_proto), success=BoolValue(value=True),
                                        playbook_execution=playbook_execution.proto)


@web_api(ExecutionsPlaybooksListRequest)
def playbooks_executions_list(request_message: ExecutionsPlaybooksListRequest) -> \
        Union[ExecutionsPlaybooksListResponse, HttpResponse]:
    meta: Meta = request_message.meta
    page: Page = meta.page
    account: Account = get_request_account()
    playbook_ids = request_message.playbook_ids
    try:
        playbook_executions = get_db_playbook_execution(account, playbook_ids=playbook_ids)
        if not playbook_executions:
            return ExecutionsPlaybooksListResponse(success=BoolValue(value=True),
                                                   message=Message(title="No Playbook Executions Found"))
        total_count = playbook_executions.count()
        playbook_executions = playbook_executions.order_by('-created_at')
        playbook_executions = filter_page(playbook_executions, page)
        pbe_protos = [pbe.proto_partial for pbe in playbook_executions]
        return ExecutionsPlaybooksListResponse(meta=get_meta(page=page, total_count=total_count),
                                               success=BoolValue(value=True), playbook_executions=pbe_protos)
    except Exception as e:
        return ExecutionPlaybookGetResponse(success=BoolValue(value=False),
                                            message=Message(title="Error", description=str(e)))


@account_post_api(ExecutePlaybookRequest)
def playbooks_api_execute(request_message: ExecutePlaybookRequest) -> Union[ExecutePlaybookResponse, HttpResponse]:
    account: Account = get_request_account()
    user = get_api_token_user()
    meta: Meta = request_message.meta
    time_range: TimeRange = meta.time_range
    current_time = current_epoch_timestamp()
    if not time_range.time_lt or not time_range.time_geq:
        time_range = TimeRange(time_geq=int(current_time - 14400), time_lt=int(current_time))
    playbook_id = request_message.playbook_id.value
    if not playbook_id:
        return ExecutePlaybookResponse(meta=get_meta(tr=time_range), success=BoolValue(value=False),
                                       message=Message(title="Invalid Request", description="Missing playbook_id"))
    playbook_run_uuid = f'{str(current_time)}_{account.id}_{playbook_id}_pb_run'
    try:
        playbook_execution = create_playbook_execution(account, time_range, playbook_id, playbook_run_uuid, user.email)
    except Exception as e:
        logger.error(e)
        return ExecutePlaybookResponse(success=BoolValue(value=False),
                                       message=Message(title="Error", description=str(e)))

    saved_task = get_or_create_task(execute_playbook.__name__, account.id, playbook_id, playbook_execution.id,
                                    proto_to_dict(time_range))
    if saved_task:
        if not check_scheduled_or_running_task_run_for_task(saved_task):
            current_date_time = current_datetime()
            task = execute_playbook.delay(account.id, playbook_id, playbook_execution.id, proto_to_dict(time_range))
            try:
                saved_task_run = TaskRun.objects.create(task=saved_task, task_uuid=task.id,
                                                        status=PeriodicTaskStatus.SCHEDULED,
                                                        account_id=account.id,
                                                        scheduled_at=current_date_time)
            except Exception as e:
                logger.error(f"Exception occurred while saving task run for account: {account.id}, "
                             f"task: {saved_task.id}, error: {e}")
    else:
        logger.error(f"Failed to create task for playbook execution: {playbook_run_uuid}")
        return ExecutePlaybookResponse(meta=get_meta(tr=time_range), success=BoolValue(value=False),
                                       message=Message(title="Error",
                                                       description="Failed to create task for playbook execution"))

    return ExecutePlaybookResponse(meta=get_meta(tr=time_range), success=BoolValue(value=True),
                                   playbook_run_id=StringValue(value=playbook_run_uuid))


@account_get_api()
def playbooks_api_execution_get(request_message: HttpRequest) -> Union[ExecutionPlaybookAPIGetResponse, HttpResponse]:
    account: Account = get_request_account()
    query_dict = request_message.GET
    if 'playbook_run_id' not in query_dict:
        return ExecutionPlaybookAPIGetResponse(success=BoolValue(value=False), message=Message(title="Invalid Request",
                                                                                               description="Missing playbook_run_id"))
    request_dict = dict(query_dict)
    playbook_run_id = request_dict.get('playbook_run_id')
    if isinstance(playbook_run_id, list):
        playbook_run_ids = playbook_run_id
    else:
        playbook_run_ids = [playbook_run_id]
    try:
        playbook_executions = get_db_playbook_execution(account, playbook_run_ids=playbook_run_ids)
        if not playbook_executions:
            return ExecutionPlaybookAPIGetResponse(success=BoolValue(value=False), message=Message(title="Error",
                                                                                                   description="Playbook Execution not found"))
    except Exception as e:
        return ExecutionPlaybookAPIGetResponse(success=BoolValue(value=False),
                                               message=Message(title="Error", description=str(e)))

    pe_protos = []
    for pe in playbook_executions:
        pe_protos.append(pe.proto)
    return ExecutionPlaybookAPIGetResponse(success=BoolValue(value=True), playbook_executions=pe_protos)
