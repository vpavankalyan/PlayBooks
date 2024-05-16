# Generated by Django 4.1.13 on 2024-05-11 11:26

from django.db import migrations


class RebuildIndexes(migrations.RunSQL):
    def __init__(self):
        super().__init__(sql=[
            "REINDEX TABLE executor_playbooktaskdefinition;",
            "REINDEX TABLE executor_playbookstep;",
            "REINDEX TABLE  executor_playbook;",
        ])


class Migration(migrations.Migration):
    dependencies = [
        ('executor', '0019_remove_playbooktaskdefinition_is_active'),
    ]

    operations = [
        RebuildIndexes(),
    ]