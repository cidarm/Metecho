# Generated by Django 2.2.2 on 2019-06-24 17:51

import django.contrib.postgres.fields
import hashid_field.field
from django.db import migrations, models

import sfdo_template_helpers.fields

ALPHABET = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"


class Migration(migrations.Migration):

    dependencies = [("api", "0001_initial")]

    operations = [
        migrations.CreateModel(
            name="Product",
            fields=[
                (
                    "id",
                    hashid_field.field.HashidAutoField(
                        alphabet=ALPHABET,
                        min_length=7,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("name", models.CharField(max_length=50, unique=True)),
                ("repo_name", models.SlugField(unique=True)),
                ("version_number", models.CharField(max_length=50)),
                ("description", sfdo_template_helpers.fields.MarkdownField()),
                ("is_managed", models.BooleanField(default=False)),
            ],
            options={"abstract": False},
        )
    ]
