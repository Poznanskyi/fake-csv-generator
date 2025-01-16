from django.db import models
from django.contrib.auth.models import User


class Schema(models.Model):
    name = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="schemas")
    created_at = models.DateTimeField(auto_now_add=True)


class Column(models.Model):
    DATA_TYPES = [
        ("string", "String"),
        ("integer", "Integer"),
        ("date", "Date"),
    ]

    name = models.CharField(max_length=255)
    date_type = models.CharField(max_length=50, choices= DATA_TYPES)
    schema = models.ForeignKey(Schema, on_delete=models.CASCADE, related_name="columns")
