# Generated by Django 4.1.13 on 2024-06-17 09:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_userinvitation'),
        ('connectors', '0014_alter_connector_connector_type_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='PagerDutyConnectorDataReceived',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('incident_id', models.CharField(blank=True, db_index=True, max_length=255, null=True)),
                ('incident_created_at', models.DateTimeField(blank=True, db_index=True, null=True)),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.account')),
                ('connector', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='connectors.connector')),
            ],
        ),
    ]