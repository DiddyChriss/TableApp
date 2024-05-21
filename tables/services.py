import logging
from django.db import connection, models
from tables.models import DynamicTable


logger = logging.getLogger(__name__)


class DynamicTableService:

    @staticmethod
    def _get_field_instance(field_type):

        field_type_map = {
            'string': models.CharField(max_length=255, null=True),
            'number': models.IntegerField(null=True),
            'boolean': models.BooleanField(default=True),
        }

        try:
            return field_type_map[field_type]
        except KeyError:
            raise ValueError(f"Unsupported field type {field_type}")

    @staticmethod
    def create_or_update_model(table_name: str, schema: dict, id: int = None) -> type(models.Model):

        attributes = {
            "__module__": "tables.models",
            "__str__": lambda self: f"{self.id}",
        }

        for field_name, field_type in schema.items():
            attributes[field_name] = DynamicTableService._get_field_instance(field_type)

        model = type(table_name, (models.Model,), attributes)

        with connection.schema_editor() as schema_editor:
            try:
                if id:
                    schema_editor.delete_model(model)

                    dynamic_table = DynamicTable.objects.get(id=id, name=table_name)

                    schema_editor.create_model(model)
                    dynamic_table.schema = schema
                    dynamic_table.save()
                else:
                    schema_editor.create_model(model)
                    DynamicTable.objects.create(name=table_name, schema=schema)
            except Exception as e:
                logger.error(f"Failed to create or update model {table_name}: {e}")
                raise

        return model
