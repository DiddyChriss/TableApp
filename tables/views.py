from django.apps import apps
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import DynamicTable
from .serializers import get_dynamic_serializer
from .services import DynamicTableService


# TODO: Adjust Swagger Schema with `@extend_schema` for required endpoints.


class TableAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request: Request) -> Response:
        try:
            name = request.data.get("name")
            schema = request.data.get("fields")

            DynamicTableService.create_or_update_model(name, schema)

            return Response({"message": "Table has been created"}, status=status.HTTP_201_CREATED)
        except ValueError as e:
            return Response({"message": str(e)}, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request: Request, id: int) -> Response:
        try:
            name = request.data.get("name")
            schema = request.data.get("fields")

            DynamicTableService.create_or_update_model(name, schema, id)
            return Response({"message": "Table updated successfully"}, status=status.HTTP_200_OK)
        except ValueError as e:
            return Response({"message": str(e)}, status=status.HTTP_400_BAD_REQUEST)


class TableRowAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request: Request, id: int) -> Response:
        try:
            dynamic_table = DynamicTable.objects.get(id=id)
            model = apps.get_model('tables', dynamic_table.name)
            serializer = get_dynamic_serializer(model)(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except DynamicTable.DoesNotExist:
            return Response("Dynamic Table not found", status=status.HTTP_404_NOT_FOUND)

    def get(self, request: Request, id: int) -> Response:
        try:
            dynamic_table = DynamicTable.objects.get(id=id)
            model = apps.get_model("tables", dynamic_table.name)
            instances = model.objects.all()
            serializer = get_dynamic_serializer(model)(instances, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except DynamicTable.DoesNotExist:
            return Response("Dynamic Table not found", status=status.HTTP_404_NOT_FOUND)
