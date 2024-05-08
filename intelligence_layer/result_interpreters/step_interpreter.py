import json
import logging

from google.protobuf.wrappers_pb2 import StringValue

from connectors.crud.connectors_crud import get_db_connectors, get_db_account_connector_keys
from integrations_api_processors.openai_api_processor import OpenAiApiProcessor
from protos.connectors.connector_pb2 import ConnectorType, ConnectorKey as ConnectorKeyProto
from protos.playbooks.intelligence_layer.interpreter_pb2 import Interpretation as InterpretationProto
from protos.playbooks.playbook_pb2 import PlaybookStepDefinition as PlaybookStepDefinitionProto

logger = logging.getLogger(__name__)


def basic_step_summariser(step: PlaybookStepDefinitionProto,
                          task_interpretations: [InterpretationProto]) -> InterpretationProto:
    return InterpretationProto()


def llm_chat_gpt_step_summariser(step: PlaybookStepDefinitionProto,
                                 task_interpretations: [InterpretationProto]) -> InterpretationProto:
    if len(task_interpretations) <= 1:
        return InterpretationProto()
    open_ai_integration = get_db_connectors(connector_type=ConnectorType.OPEN_AI, is_active=True)
    if not open_ai_integration:
        logger.error('Aborting LLM step summariser. OpenAI integration is not set.')
        return InterpretationProto()
    open_ai_integration = open_ai_integration.first()
    open_ai_api_key = get_db_account_connector_keys(open_ai_integration.account, open_ai_integration.id,
                                                    key_type=ConnectorKeyProto.KeyType.OPEN_AI_API_KEY)
    if not open_ai_api_key:
        logger.error('Aborting LLM step summariser. OpenAI API key is not set.')
        return InterpretationProto()
    open_ai_api_key = open_ai_api_key.first().key
    try:
        keys = """
                anomaly_detected:boolean
                description:string
            """

        system_prompt = """
                            You are a DevOps engineer who is an expert at interpreting metric results and identifying any 
                            correlations between them. These metrics are generated by tools and services that you use to 
                            deploy and monitor your applications or services. Study all the metrics and their 
                            interpretation keeping in mind that they are related and intentionally sent together. 
                            Identify and state if there is any anomaly here. You will be given images of the metrics data. 
                            You will need to return a JSON object with the following keys:
                            {keys}
                """.format(keys=keys)

        gpt_prompt = []
        for ti in task_interpretations:
            if ti.type == InterpretationProto.Type.IMAGE:
                prompt = ti.title.value
                description = ti.description.value
                if description:
                    prompt += f' {description}'
                summary = ti.summary.value
                if summary:
                    prompt += f' {summary}'
                image_url = ti.image_url.value

                gpt_prompt.append(
                    {
                        "type": "text",
                        "text": f"This image describes {prompt}"
                    }
                )
                gpt_prompt.append({
                    "type": "image_url",
                    "image_url": {
                        "url": image_url,
                    },
                })

        if not gpt_prompt:
            return task_interpretations

        gpt_prompt.append({
            "type": "text",
            "text": "These are all the images and context of the image. Only send "
                    "the keys that are requested. Do not send more keys or keys with empty or N/A values. Strictly "
                    "do not respond with empty strings or N/A or 'No Data' as key values."
        })

        open_ai_client = OpenAiApiProcessor(open_ai_api_key=open_ai_api_key)
        gpt_response = open_ai_client.chat_completions_create(
            model="gpt-4-turbo",
            response_format={"type": "json_object"},
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": gpt_prompt}
            ]
        )
        logger.info(gpt_response.choices[0])
        logger.info(gpt_response.choices[0].message.content)
        gpt_response = gpt_response.choices[0].message.content
        gpt_response = json.loads(gpt_response)
        inference = {'anomaly_detected': gpt_response['anomaly_detected'], 'description': gpt_response['description']}

        title = f'`Step Summary`'
        description = f'`Description`: {inference["description"]}'
        summary = f'`Anomaly Detected`: {inference["anomaly_detected"]}'

        step_summary = InterpretationProto(
            type=InterpretationProto.Type.SUMMARY,
            title=StringValue(value=title),
            description=StringValue(value=description),
            summary=StringValue(value=summary),
        )
        return step_summary
    except Exception as e:
        logger.error(f'Error summarising step: {e}')
        return InterpretationProto()
