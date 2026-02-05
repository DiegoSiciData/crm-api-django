from django.contrib import admin
from .models import Client

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'email', 'phone', 'company', 'created_at')
    search_fields = ('name', 'email')
