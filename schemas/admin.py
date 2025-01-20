from django.contrib import admin
from .models import DataSchema, DataColumn, GeneratedData


admin.site.register(DataSchema)
admin.site.register(DataColumn)
admin.site.register(GeneratedData)

