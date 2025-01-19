from django.urls import path
from . import views

urlpatterns = [
    path("create/", views.create_schema, name="create_schema"),
    path("schema/<int:schema_id>/columns", views.add_columns, name="add_columns"),
    path("schema/<int:schema_id>/generate", views.generate_data, name="generate_data"),
]