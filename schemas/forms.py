from django import forms
from .models import Schema, Column


class SchemasForm(forms.ModelForm):
    class Meta:
        model = Schema
        fields = ["name"]


class ColumnForm(forms.ModelForm):
    class Meta:
        model = Column
        fields = ["name", "data_type"]