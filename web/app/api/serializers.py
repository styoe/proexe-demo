from rest_framework import serializers
from .models import Table


class TableSerializer(serializers.ModelSerializer):
    class Meta:
        model = Table
        fields = ["name", "fields", "created", "updated"]


def get_dynamic_serializer(DynModel, dyn_fields):
    class DynSerializer(serializers.ModelSerializer):
        class Meta:
            model = DynModel
            fields = dyn_fields

    return DynSerializer