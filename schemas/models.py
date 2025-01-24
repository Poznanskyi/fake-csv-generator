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
        ('full_name', 'Full Name'),
        ('job', 'Job'),
        ('email', 'Email'),
        ('domain_name', 'Domain Name'),
        ('phone_number', 'Phone Number'),
        ('company_name', 'Company Name'),
        ('text', 'Text'),
        ('integer', 'Integer'),
        ('address', 'Address'),
        ('date', 'Date'),
    ]

    schema = models.ForeignKey(DataSchema, on_delete=models.CASCADE, related_name="columns")
    name = models.CharField(max_length=100)
    data_type = models.CharField(max_length=20, choices=DATA_TYPES)

    def __str__(self):
        return f"{self.name} ({self.data_type})"


class GeneratedData(models.Model):
    schema = models.ForeignKey(DataSchema, on_delete=models.CASCADE)
    data = models.JSONField()

    def __str__(self):
        return f"Generated Data for {self.schema.name}"

