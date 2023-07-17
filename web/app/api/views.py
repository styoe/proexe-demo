from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Table
from .serializers import TableSerializer, get_dynamic_serializer
from .utils import (
    get_table_model_attrs_from_fields, 
    get_table_model_name_from_id, 
    get_table_model_from_attrs, 
    create_table_from_dynamic_model, 
    update_table_from_dynamic_model
)


class TableApiView(APIView):
    def get(self, request, table_id=None):
        tables = Table.objects.filter() if table_id is None else Table.objects.filter(id=table_id)
        serializer = TableSerializer(tables, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = TableSerializer(data=request.data)
        if not serializer.is_valid():
           return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        try:
          table_attrs = get_table_model_attrs_from_fields(serializer.validated_data["fields"])
        except ValueError as e:
           return Response(str(e), status=status.HTTP_400_BAD_REQUEST)

        serializer.save()

        dyn_model_name = get_table_model_name_from_id(serializer.instance.id)
        dyntablemodel = get_table_model_from_attrs(dyn_model_name, table_attrs)
        create_table_from_dynamic_model(dyntablemodel)
            
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    def put(self, request, table_id=None):
        table = Table.objects.filter(id=table_id).first()
        if table is None:
           return Response("Table not found", status=status.HTTP_404_NOT_FOUND)
        
        serializer = TableSerializer(table, data=request.data)
        if not serializer.is_valid():
           return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        try:
          table_attrs = get_table_model_attrs_from_fields(serializer.validated_data["fields"])
        except ValueError as e:
           return Response(str(e), status=status.HTTP_400_BAD_REQUEST)

        serializer.update(table, serializer.validated_data)

        dyn_model_name = get_table_model_name_from_id(serializer.instance.id)
        DynTableModel = get_table_model_from_attrs(dyn_model_name, table_attrs)
        update_table_from_dynamic_model(DynTableModel)

        return Response(serializer.data, status=status.HTTP_201_CREATED)


class TableRowApiView(APIView):
    def post(self, request, table_id=None):
        table = Table.objects.filter(id=table_id).first()
        if table is None:
           return Response("Table not found", status=status.HTTP_404_NOT_FOUND)

        table_attrs = get_table_model_attrs_from_fields(table.fields)
        dyn_model_name = get_table_model_name_from_id(table_id)
        DynTableModel = get_table_model_from_attrs(dyn_model_name, table_attrs)
        DynSerializer = get_dynamic_serializer(DynTableModel, [k["name"] for k in table.fields])

        data = request.data
        serializer = DynSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class TableRowsApiView(APIView):
    def get(self, request, table_id=None):
        table = Table.objects.filter(id=table_id).first()
        if table is None:
           return Response("Table not found", status=status.HTTP_404_NOT_FOUND)
        
        table_attrs = get_table_model_attrs_from_fields(table.fields)
        dyn_model_name = get_table_model_name_from_id(table_id)
        DynTableModel = get_table_model_from_attrs(dyn_model_name, table_attrs)
        rows = DynTableModel.objects.filter()

        DynSerializer = get_dynamic_serializer(DynTableModel, [k["name"] for k in table.fields])
        serializer = DynSerializer(rows, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

