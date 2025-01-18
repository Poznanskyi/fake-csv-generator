from django import forms
from .models import DataSchema, DataColumn


class DataSchemaForm(forms.ModelForm):
    class Meta:
        model = DataSchema
        fields = ["name"]


class DataColumnForm(forms.ModelForm):
    class Meta:
        model = DataColumn
        fields = ["name", "data_type"]