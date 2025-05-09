
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import Group

from core.models import User, Departement, Role



@admin.register(Role)
class RoleAdmin(admin.ModelAdmin):
    list_display = ('name',)


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        exclude = ('password1', 'password2')


@admin.register(User)
class UserAdmin(UserAdmin):
    site_header = "Monty Python administration"



@admin.register(Departement)
class DepartementAdmin(admin.ModelAdmin):
    list_display = ('name',)



