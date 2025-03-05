
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin, GroupAdmin
from django.contrib.auth.models import Group

from core.models import User


@admin.register(User)
class UserAdmin(UserAdmin):
    site_header = "Monty Python administration"



