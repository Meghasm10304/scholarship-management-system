from django import forms
from .models import StudentProfile, ScholarshipApplication

class StudentProfileForm(forms.ModelForm):
    class Meta:
        model = StudentProfile
        fields = ['student_id', 'date_of_birth', 'address', 'city', 'state', 
                 'zip_code', 'gpa', 'major', 'graduation_year', 'resume', 'transcript']
        widgets = {
            'date_of_birth': forms.DateInput(attrs={'type': 'date'}),
            'address': forms.Textarea(attrs={'rows': 3}),
        }

class ScholarshipApplicationForm(forms.ModelForm):
    class Meta:
        model = ScholarshipApplication
        fields = ['essay', 'additional_documents']
        widgets = {
            'essay': forms.Textarea(attrs={'rows': 8}),
        }
