
from django.contrib import admin
from .models import Project


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'priority', 'created_by', 'created_at')
    list_filter = ('status', 'priority', 'created_at')
    search_fields = ('title', 'description')