from django.contrib import admin
from .models import SerialKey,UserKeyUsage
# Register your models here.
admin.site.register(SerialKey)
admin.site.register(UserKeyUsage)