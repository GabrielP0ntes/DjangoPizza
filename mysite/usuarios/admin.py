from django.contrib import admin
from .models import usuario

@admin.register(usuario)
class UsuarioAdmin(admin.ModelAdmin):
    readonly_fields = ('nome', 'email', 'senha')
