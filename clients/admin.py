from django.contrib import admin
from .models import Client


class ClientAdmin(admin.ModelAdmin):
    list_display = ("name", "animal", "joined_date",)


admin.site.register(Client, ClientAdmin)