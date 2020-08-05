import uuid

from django.db import models
from django.core.validators import EmailValidator
from ares_util.validators import czech_company_id_ares_api_validator


class User(models.Model):
    guid = models.UUIDField(unique=True, editable=False, default=uuid.uuid4)
    jméno = models.CharField(max_length=255)
    email = models.EmailField(
        max_length=255, validators=(EmailValidator,), unique=True, null=True, blank=True
    )
    ičo = models.CharField(
        max_length=8, validators=(czech_company_id_ares_api_validator,), unique=True
    )
