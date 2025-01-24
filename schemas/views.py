import random

from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render, redirect
from faker import Faker

from .models import DataSchema, GeneratedData
from .forms import DataSchemaForm, DataColumnForm

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
        if data_type == "full_name":
            generated_data[column.name] = fake.name()
        elif data_type == "job":
            generated_data[column.name] = fake.job()
        elif data_type == "email":
            generated_data[column.name] = fake.email()
        elif data_type == "domain_name":
            generated_data[column.name] = fake.domain_name()
        elif data_type == "phone_number":
            generated_data[column.name] = fake.phone_number()
        elif data_type == "company_name":
            generated_data[column.name] = fake.company()
        elif data_type == "text":
            generated_data[column.name] = fake.text(max_nb_chars=200)
        elif data_type == "integer":
            min_val = 1
            max_val = 1000
            generated_data[column.name] = random.randint(min_val, max_val)
        elif data_type == "address":
            generated_data[column.name] = fake.address()
        elif data_type == "date":
            generated_data[column.name] = fake.date_this_decade()

    GeneratedData.objects.create(schema=schema, data=generated_data)

    return JsonResponse(generated_data)
