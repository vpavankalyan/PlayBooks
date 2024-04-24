# Generated by Django 4.1.4 on 2024-04-22 12:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('executor', '0003_playbookexecution_time_range_and_more'),
        ('accounts', '0002_userinvitation'),
    ]

    operations = [
        migrations.CreateModel(
            name='Workflow',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True, null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('created_by', models.TextField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('schedule_type', models.IntegerField(choices=[(0, 'UNKNOWN'), (1, 'ONE_OFF'), (2, 'PERIODIC')], db_index=True)),
                ('schedule', models.JSONField()),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.account')),
            ],
        ),
        migrations.CreateModel(
            name='WorkflowAction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.IntegerField(choices=[(0, 'UNKNOWN'), (1, 'NOTIFY')], db_index=True)),
                ('action', models.JSONField()),
                ('action_md5', models.CharField(db_index=True, max_length=256)),
                ('is_active', models.BooleanField(default=True)),
                ('created_by', models.TextField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.account')),
            ],
            options={
                'unique_together': {('account', 'type', 'action_md5', 'created_by')},
            },
        ),
        migrations.CreateModel(
            name='WorkflowEntryPoint',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.IntegerField(choices=[(0, 'UNKNOWN'), (1, 'API'), (2, 'ALERT')], db_index=True)),
                ('entry_point', models.JSONField()),
                ('entry_point_md5', models.CharField(db_index=True, max_length=256)),
                ('is_active', models.BooleanField(default=True)),
                ('created_by', models.TextField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.account')),
            ],
            options={
                'unique_together': {('account', 'type', 'entry_point_md5', 'created_by')},
            },
        ),
        migrations.CreateModel(
            name='WorkflowPlayBookMapping',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.account')),
                ('playbook', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='executor.playbook')),
                ('workflow', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='workflows.workflow')),
            ],
            options={
                'unique_together': {('account', 'workflow', 'playbook')},
            },
        ),
        migrations.CreateModel(
            name='WorkflowEntryPointMapping',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.account')),
                ('entry_point', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='workflows.workflowentrypoint')),
                ('workflow', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='workflows.workflow')),
            ],
            options={
                'unique_together': {('account', 'workflow', 'entry_point')},
            },
        ),
        migrations.CreateModel(
            name='WorkflowActionMapping',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.account')),
                ('action', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='workflows.workflowaction')),
                ('workflow', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='workflows.workflow')),
            ],
            options={
                'unique_together': {('account', 'workflow', 'action')},
            },
        ),
        migrations.AddField(
            model_name='workflow',
            name='actions',
            field=models.ManyToManyField(related_name='workflow_actions', through='workflows.WorkflowActionMapping', to='workflows.workflowaction'),
        ),
        migrations.AddField(
            model_name='workflow',
            name='entry_points',
            field=models.ManyToManyField(related_name='workflow_entry_points', through='workflows.WorkflowEntryPointMapping', to='workflows.workflowentrypoint'),
        ),
        migrations.AddField(
            model_name='workflow',
            name='playbooks',
            field=models.ManyToManyField(related_name='workflow_playbooks', through='workflows.WorkflowPlayBookMapping', to='executor.playbook'),
        ),
        migrations.AlterUniqueTogether(
            name='workflow',
            unique_together={('account', 'name', 'created_by')},
        ),
    ]
