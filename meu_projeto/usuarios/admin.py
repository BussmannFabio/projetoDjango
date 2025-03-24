from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    # Acrescenta os novos campos aos fieldsets do admin
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('cpf', 'rg', 'endereco', 'sexo')}),
    )
    # Inclui os novos campos também ao criar um novo usuário via admin
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('cpf', 'rg', 'endereco', 'sexo')}),
    )

admin.site.register(CustomUser, CustomUserAdmin)
