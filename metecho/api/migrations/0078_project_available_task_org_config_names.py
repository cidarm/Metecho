# Generated by Django 3.0.6 on 2020-06-01 19:57

import django.contrib.postgres.fields.jsonb
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0077_add_org_config_name_to_task"),
    ]

    operations = [
        migrations.AddField(
            model_name="project",
            name="available_task_org_config_names",
            field=django.contrib.postgres.fields.jsonb.JSONField(
                blank=True, default=list
            ),
        ),
    ]
