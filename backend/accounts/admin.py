from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CodingrushAccount

# Register your models here.

admin.site.register(CodingrushAccount, UserAdmin)
