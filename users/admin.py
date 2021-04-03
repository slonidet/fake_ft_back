from django.contrib import admin

# Register your models here.
from django.contrib.admin import ModelAdmin

from users.models import Adapter, User, License


class AdapterAdmin(ModelAdmin):
    model = Adapter


class UserAdmin(ModelAdmin):
    model = User


class LicenseAdmin(ModelAdmin):
    model = License


admin.site.register(Adapter, AdapterAdmin)
admin.site.register(User, UserAdmin)
admin.site.register(License, LicenseAdmin)
