from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import StudentProfile, ScholarshipApplication
from .forms import StudentProfileForm, ScholarshipApplicationForm
from scholarships.models import Scholarship
from django.utils import timezone

@login_required
def student_dashboard(request):
    try:
        student_profile = request.user.student_profile
    except StudentProfile.DoesNotExist:
        return redirect('create_student_profile')
    
    applications = ScholarshipApplication.objects.filter(student=student_profile)
    context = {
        'student': student_profile,
        'applications': applications,
        'total_applications': applications.count(),
        'approved_applications': applications.filter(status='approved').count(),
        'pending_applications': applications.filter(status='pending').count(),
    }
    return render(request, 'students/dashboard.html', context)

@login_required
def create_student_profile(request):
    if hasattr(request.user, 'student_profile'):
        return redirect('student_dashboard')
    
    if request.method == 'POST':
        form = StudentProfileForm(request.POST, request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
            messages.success(request, 'Your profile has been created successfully!')
            return redirect('student_dashboard')
    else:
        form = StudentProfileForm()
    
    return render(request, 'students/create_profile.html', {'form': form})

@login_required
def update_student_profile(request):
    student_profile = get_object_or_404(StudentProfile, user=request.user)
    
    if request.method == 'POST':
        form = StudentProfileForm(request.POST, request.FILES, instance=student_profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your profile has been updated successfully!')
            return redirect('student_dashboard')
    else:
        form = StudentProfileForm(instance=student_profile)
    
    return render(request, 'students/update_profile.html', {'form': form})

@login_required
def available_scholarships(request):
    student_profile = get_object_or_404(StudentProfile, user=request.user)
    scholarships = Scholarship.objects.filter(deadline__gte=timezone.now().date())

    # Get all the applications for this student
    student_applications = ScholarshipApplication.objects.filter(student=student_profile)
    applications_dict = {app.scholarship_id: app for app in student_applications}

    context = {
        'scholarships': scholarships,
        'applications_dict': applications_dict,  # pass the mapping to template
    }
    return render(request, 'students/available_scholarships.html', context)


@login_required
def scholarship_detail(request, scholarship_id):
    scholarship = get_object_or_404(Scholarship, id=scholarship_id)
    context = {
        'scholarship': scholarship
    }
    return render(request, 'students/scholarship_detail.html', context)

    
@login_required
def apply_scholarship(request, scholarship_id):
    student_profile = get_object_or_404(StudentProfile, user=request.user)
    scholarship = get_object_or_404(Scholarship, id=scholarship_id)

    # Check if already applied
    if ScholarshipApplication.objects.filter(student=student_profile, scholarship=scholarship).exists():
        messages.warning(request, 'You have already applied for this scholarship.')
        return redirect('available_scholarships')

    if request.method == 'POST':
        # Only upload documents; profile details are from student_profile
        additional_documents = request.FILES.get('additional_documents')
        application = ScholarshipApplication.objects.create(
            student=student_profile,
            scholarship=scholarship,
            additional_documents=additional_documents
        )
        messages.success(request, 'Your application has been submitted successfully!')
        return redirect('student_dashboard')

    return render(request, 'students/apply_scholarship.html', {
        'student': student_profile,
        'scholarship': scholarship
    })


@login_required
def my_applications(request):
    student_profile = get_object_or_404(StudentProfile, user=request.user)
    applications = ScholarshipApplication.objects.filter(student=student_profile)
    
    context = {
        'applications': applications,
    }
    return render(request, 'students/my_applications.html', context)

