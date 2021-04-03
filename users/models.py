import uuid

from django.db import models


# Create your models here.
class User(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=32)
    is_master = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)

    serial_number = models.CharField(max_length=10, blank=True, null=True)
    code = models.CharField(max_length=10, blank=True, null=True)

    def __str__(self):
        return self.email


class Adapter(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    serial_number = models.CharField(primary_key=True, max_length=32)
    code = models.CharField(max_length=32)


class License(models.Model):
    adapter = models.ForeignKey(Adapter, on_delete=models.CASCADE)
    license_type = models.CharField(max_length=100)
    tariff = models.CharField(max_length=100)

    calculated_price = models.FloatField(blank=True, null=True)
    is_active = models.BooleanField(default=False)
    start_date = models.DateField(blank=True, null=True)
    finish_date = models.DateField(blank=True, null=True)
