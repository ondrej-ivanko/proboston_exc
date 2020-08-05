# Generated by Django 3.0.9 on 2020-08-05 11:49

import ares_util.validators
import django.core.validators
from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="User",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "guid",
                    models.UUIDField(default=uuid.uuid4, editable=False, unique=True),
                ),
                ("jméno", models.CharField(max_length=255)),
                (
                    "email",
                    models.EmailField(
                        blank=True,
                        max_length=255,
                        null=True,
                        unique=True,
                        validators=[django.core.validators.EmailValidator],
                    ),
                ),
                (
                    "ičo",
                    models.CharField(
                        max_length=8,
                        unique=True,
                        validators=[
                            ares_util.validators.czech_company_id_ares_api_validator
                        ],
                    ),
                ),
            ],
        ),
    ]
