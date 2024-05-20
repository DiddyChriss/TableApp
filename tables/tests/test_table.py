import pytest
from django.db import models
from tables.services import DynamicTableService
from tests.test_user_setup import UserSetup


# TODO: Tests need to be extended for at least 85% coverage(especially with Exceptions).


@pytest.mark.django_db
class TestDynamicTable(UserSetup):
    def test_create_dynamic_model(self, api_client, super_user):
        schema = {
            "name": "CharField",
            "age": "IntegerField"
        }
        model = DynamicTableService.create_or_update_model("TestModel", schema)
        assert issubclass(model, models.Model)
        assert hasattr(model, "name")
        assert hasattr(model, "age")

    @pytest.mark.django_db
    def test_update_dynamic_model(self, api_client, super_user):
        initial_schema = {"name": "CharField"}
        DynamicTableService.create_or_update_model("UpdateTestModel", initial_schema)
        updated_schema = {"name": "CharField", "age": "IntegerField"}
        updated_model = DynamicTableService.create_or_update_model("UpdateTestModel", updated_schema, update=True)
        assert hasattr(updated_model, "age")

    @pytest.mark.django_db
    def test_model_field_type_is_proper(self, api_client, super_user):
        schema = {"name": "CharField", "active": "BooleanField"}
        model = DynamicTableService.create_or_update_model("FieldTypeModel", schema)
        name_field = model._meta.get_field("name")
        active_field = model._meta.get_field("active")
        assert isinstance(name_field, models.CharField)
        assert isinstance(active_field, models.BooleanField)

