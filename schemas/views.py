import random

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse

from faker import Faker

from.forms import DataSchemaForm, DataColumnForm
from .models import DataSchema, DataColumn, GeneratedData

fake = Faker()

@login_required
def create_schema(request):
    if request.method == "POST":
        form = DataSchemaForm(request.POST)
        if form.is_valid():
            schema = form.save(commit=False)
            schema.user = request.user
            schema.save()
            return redirect("add_columns", schema_id=schema.id)
    else:
        form = DataSchemaForm()
    return render(request, "schemas/create_schema.html", {"form": form})

@login_required
def add_columns(request, schema_id):
    schema = DataSchema.objects.get(id=schema_id, user=request.user)
    if request.method == "POST":
        form = DataColumnForm(request.POST)
        if form.is_valid():
            column = form.save(commit=False)
            column.schema = schema
            column.save()
            return redirect("add_columns", schema_id=schema.id)
    else:
        form = DataColumnForm()
    columns = schema.colums.all()
    return render(
        request,
        "schemas/add_columns.html",
        {"form": form, "schema": schema, "columns": columns}
    )

@login_required
def generate_data(request, schema_id):
    schema = DataSchema.objects.get(id=schema_id, user=request.user)
    columns = schema.columns.all()

    generated_data = {}
    for column in columns:
        data_type = column.data_type
        if data_type == "char":
            generated_data[column.name] = fake.word()
        elif data_type == "int":
            generated_data[column.name] = random.randint(1, 100)
        elif data_type == "date":
            generated_data[column.name] = fake.date()
        elif data_type == "float":
            generated_data[column.name] = random.uniform(1.0, 100.0)

    GeneratedData.objects.create(schema=schema, data=generated_data)

    return JsonResponse(generated_data)
