from django.contrib import admin
from core.models import DataTable

class FileAdmin(admin.ModelAdmin):
    list_display = ["image_name","objects_detected","timestamp"]
admin.site.register(DataTable, FileAdmin)