from django.urls import path, include
from .views import TableAPIView, TableRowAPIView


urlpatterns = [
    path("table/", TableAPIView.as_view()),
    path("table/<int:id>", TableAPIView.as_view()),
    path("table/<int:id>/row", TableRowAPIView.as_view()),
    path("table/<int:id>/rows", TableRowAPIView.as_view()),
]
