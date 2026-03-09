from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Scholarship

@login_required
def scholarship_list(request):
    scholarships = Scholarship.objects.filter(is_active=True)
    return render(request, 'scholarships/list.html', {'scholarships': scholarships})

@login_required
def scholarship_detail(request, pk):
    scholarship = get_object_or_404(Scholarship, pk=pk)
    return render(request, 'scholarships/detail.html', {'scholarship': scholarship})
