from django.db import models
from django.db import connections


def get_table_model_attrs_from_fields(fields):
    attrs = {
      "__module__": "app.api.models"
    }

    if not fields:
        raise ValueError(f"Fields should have at least one column definition.") 

    # TODO: Add custom schema validator in Table model for fields
    for field in fields:
        if field["type"] == "string":
            attrs[field["name"]] = models.CharField()
        elif field["type"] == "number":
            attrs[field["name"]] = models.IntegerField()
        elif field["type"] == "boolean":
            attrs[field["name"]] = models.BooleanField()
        else: 
            raise ValueError(f"Table field {field['name']} has unsupported type of {field['type']}. Supported types are 'string', 'number' and 'boolean'.") 

    return attrs


def get_table_model_name_from_id(id):
    return f"DynamicTable_{id}"  


def get_table_model_from_attrs(name, attrs):
    DynamicTable = type(name, (models.Model,), attrs)
    return DynamicTable


def create_table_from_dynamic_model(DynModel):
    connection = connections['default']
    with connection.schema_editor() as schema_editor:
      schema_editor.create_model(DynModel)
    # TODO: check to add this as migration?


def update_table_from_dynamic_model(DynModel):
    connection = connections['default']
    with connection.schema_editor() as schema_editor:
      # TODO: Compare schemas and use schema_editor.alter_field
      schema_editor.delete_model(DynModel)
      schema_editor.create_model(DynModel)
    # TODO: check to add this as migration?
    