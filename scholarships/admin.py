from django.contrib import admin
from .models import Scholarship

@admin.register(Scholarship)
class ScholarshipAdmin(admin.ModelAdmin):
    list_display = ['title', 'provider', 'amount', 'deadline', 'is_active']
    list_filter = ['is_active', 'deadline', 'provider']
    search_fields = ['title', 'provider', 'description']
    date_hierarchy = 'deadline'
