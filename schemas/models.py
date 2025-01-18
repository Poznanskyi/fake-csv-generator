from django.db import models
from django.contrib.auth.models import User


class DataSchema(models.Model):
    name = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class DataColumn(models.Model):
    DATA_TYPES = [
        ("char", "Character"),
        ("string", "String"),
        ("integer", "Integer"),
        ("date", "Date"),
    ]

    schema = models.ForeignKey(DataSchema, on_delete=models.CASCADE, related_name="columns")
    name = models.CharField(max_length=100)
    date_type = models.CharField(max_length=10, choices= DATA_TYPES)

    def __str__(self):
        return f"{self.name} ({self.date_type})"


class GeneratedData(models.Model):
    schema = models.ForeignKey(DataSchema, on_delete=models.CASCADE)
    data = models.JSONField()

    def __str__(self):
        return f"Generated Data for {self.schema.name}"

