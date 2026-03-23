from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.views.generic import TemplateView
from .forms import SignUpForm, ContactForm
from django.utils import timezone
from scholarships.models import Scholarship
from django.db.models import Q

class HomeView(TemplateView):
    template_name = 'accounts/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        query = self.request.GET.get('q')

        # Latest
        context['latest_scholarships'] = Scholarship.objects.order_by('-created_at')[:2]

        # Expiring
        context['expiring_soon'] = Scholarship.objects.filter(
            deadline__gte=timezone.now().date()
        ).order_by('deadline')[:2]

        # ✅ SEARCH LOGIC
        if query:
            context['search_results'] = Scholarship.objects.filter(
                Q(title__icontains=query) |
                Q(description__icontains=query)
            )
        else:
            context['search_results'] = None

        context['query'] = query

        return context

class AboutView(TemplateView):
    template_name = 'accounts/about.html'

class FAQView(TemplateView):
    template_name = 'accounts/faq.html'

class TermsView(TemplateView):
    template_name = 'accounts/terms.html'

class PrivacyView(TemplateView):
    template_name = 'accounts/privacy.html'

def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, f'Welcome {username}! Your account has been created successfully.')
            return redirect('student_dashboard')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = SignUpForm()
    return render(request, 'accounts/signup.html', {'form': form})
    
def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Process the contact form (send email, save to database, etc.)
            messages.success(request, 'Thank you for contacting us! We will respond soon.')
            return redirect('home')
    else:
        form = ContactForm()
    return render(request, 'accounts/contact.html', {'form': form})