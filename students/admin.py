from django.contrib import admin
from .models import StudentProfile, Application

@admin.register(StudentProfile)
class StudentProfileAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'college_name', 'course', 'annual_income')
    search_fields = ('full_name', 'college_name')


@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
    list_display = ('student', 'scholarship', 'status', 'applied_on')
    list_editable = ('status',)
    list_filter = ('status',)

