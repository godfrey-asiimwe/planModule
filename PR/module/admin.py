from django.contrib import admin
from .models import Project


class question(admin.ModelAdmin):
    list_display = (
       'id','name', 'description','type')
    search_fields = ['name']


admin.site.register(Project, question)