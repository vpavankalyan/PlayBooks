# Generated by Django 4.1.13 on 2024-06-17 10:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('connectors', '0016_pagerdutyconnectordatareceived_title'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pagerdutyconnectordatareceived',
            name='account',
        ),
        migrations.RemoveField(
            model_name='pagerdutyconnectordatareceived',
            name='connector',
        ),
    ]