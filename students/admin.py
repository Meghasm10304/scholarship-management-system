from django.contrib import admin
from .models import StudentProfile, ScholarshipApplication


@admin.register(StudentProfile)
class StudentProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'student_id', 'major', 'gpa', 'graduation_year']
    list_filter = ['major', 'graduation_year']
    search_fields = ['user__username', 'user__email', 'student_id', 'major']


@admin.register(ScholarshipApplication)
class ScholarshipApplicationAdmin(admin.ModelAdmin):
    list_display = ['student', 'scholarship', 'status', 'applied_at']
    list_filter = ['status', 'applied_at']
    search_fields = ['student__user__username', 'scholarship__title']
    date_hierarchy = 'applied_at'
    
    actions = ['approve_applications', 'reject_applications']
    
    def approve_applications(self, request, queryset):
        queryset.update(status='approved')
    approve_applications.short_description = "Approve selected applications"
    
    def reject_applications(self, request, queryset):
        queryset.update(status='rejected')
    reject_applications.short_description = "Reject selected applications"

