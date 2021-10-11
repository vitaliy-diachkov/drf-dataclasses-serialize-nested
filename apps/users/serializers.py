import decimal
import uuid
import datetime

import rest_framework.fields
from rest_framework import serializers
from rest_framework_dataclasses import fields
from rest_framework_dataclasses.serializers import DataclassSerializer

from apps.users.dataclasses import SocialSecurityNumber, User
from apps.users.fields import SocialSecurityNumberField


class CustomDataclassSerializer(DataclassSerializer):
    serializer_field_mapping = {
        int:                  rest_framework.fields.IntegerField,
        float:                rest_framework.fields.FloatField,
        bool:                 rest_framework.fields.BooleanField,
        str:                  rest_framework.fields.CharField,
        decimal.Decimal:      fields.DefaultDecimalField,
        datetime.date:        rest_framework.fields.DateField,
        datetime.datetime:    rest_framework.fields.DateTimeField,
        datetime.time:        rest_framework.fields.TimeField,
        datetime.timedelta:   rest_framework.fields.DurationField,
        uuid.UUID:            rest_framework.fields.UUIDField,
        dict:                 rest_framework.fields.DictField,
        list:                 rest_framework.fields.ListField,
        SocialSecurityNumber: SocialSecurityNumberField
    }

    @property
    def serializer_dataclass_field(self):
        return CustomDataclassSerializer
