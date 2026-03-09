from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .models import StudentProfile, Application
from scholarships.models import Scholarship

@login_required
def dashboard(request):
    profile, created = StudentProfile.objects.get_or_create(
        user=request.user
    )

    if not profile.full_name:
        return redirect('profile')

    scholarships = Scholarship.objects.all()

    applied_ids = Application.objects.filter(
        student=profile
    ).values_list('scholarship_id', flat=True)

    return render(request, 'students/dashboard.html', {
        'profile': profile,
        'scholarships': scholarships,
        'applied_ids': applied_ids
    })




@login_required
def profile_view(request):
    profile, created = StudentProfile.objects.get_or_create(
        user=request.user
    )

    if request.method == 'POST':
        profile.full_name = request.POST.get('full_name')
        profile.dob = request.POST.get('dob')
        profile.gender = request.POST.get('gender')
        profile.category = request.POST.get('category')
        profile.college_name = request.POST.get('college_name')
        profile.course = request.POST.get('course')
        profile.year_of_study = request.POST.get('year_of_study')
        profile.annual_income = request.POST.get('annual_income')

        if request.FILES.get('aadhaar'):
            profile.aadhaar = request.FILES.get('aadhaar')

        if request.FILES.get('marksheet'):
            profile.marksheet = request.FILES.get('marksheet')

        profile.save()
        return redirect('dashboard')

    return render(request, 'students/profile.html', {
        'profile': profile
    })



def apply_scholarship(request, id):
    profile = StudentProfile.objects.get(user=request.user)
    scholarship = Scholarship.objects.get(id=id)

    if Application.objects.filter(
        student=profile,
        scholarship=scholarship
    ).exists():
        messages.warning(
            request,
            "⚠️ You have already applied for this scholarship."
        )
    else:
        Application.objects.create(
            student=profile,
            scholarship=scholarship
        )
        messages.success(
            request,
            "✅ Scholarship applied successfully!"
        )

    return redirect('dashboard')





def available_scholarships(request):
    profile = StudentProfile.objects.get(user=request.user)

    scholarships = Scholarship.objects.all()

    applied_ids = Application.objects.filter(
        student=profile
    ).values_list('scholarship_id', flat=True)

    context = {
        'scholarships': scholarships,
        'applied_ids': applied_ids
    }

    return render(request, 'available_scholarships.html', context)