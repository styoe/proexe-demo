from django.urls import path
from .views import (
    TableApiView,
    TableRowApiView,
    TableRowsApiView
)

table_api_view = TableApiView.as_view()
table_row_api_view = TableRowApiView.as_view()
table_rows_api_view = TableRowsApiView.as_view()

urlpatterns = [
    path("table", table_api_view),
    path("table/<int:table_id>/", table_api_view),
    path("table/<int:table_id>/row", table_row_api_view),
    path("table/<int:table_id>/rows", table_rows_api_view),
]
