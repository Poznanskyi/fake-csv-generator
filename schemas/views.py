import random

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse

from faker import Faker

from.forms import DataSchemaForm, DataColumnForm
from .models import DataSchema, DataColumn, GeneratedData


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
