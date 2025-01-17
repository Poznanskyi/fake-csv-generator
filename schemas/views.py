from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from.forms import SchemasForm, ColumnForm
from .models import Schema, Column


@login_required
def create_schema(request):
    if request.method == "POST":
        schema_form = SchemasForm(request.POST)
        if schema_form.is_valid():
            schema = schema_form.save(commit=False)
            schema.user = request.user
            schema.save()
            return redirect("list_schemas")
    else:
        schema_form = SchemasForm
    return render(request, "create_schema.html", {"form": schema_form})

@login_required
def list_schemas(request):
    schemas = Schema.object.filter(user=request.user)
    return render(request, "list_schemas.html", {"schemas": schemas})
