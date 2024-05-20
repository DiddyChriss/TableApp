from rest_framework import serializers


def get_dynamic_serializer(model_class):
    """ Create a serializer class for a dynamically created model class """

    class DynamicTableSerializer(serializers.ModelSerializer):
        class Meta:
            model = model_class
            fields = "__all__"

    return DynamicTableSerializer
