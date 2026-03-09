from django.urls import path
from .views import dashboard, profile_view, apply_scholarship

urlpatterns = [
    path('dashboard/', dashboard, name='dashboard'),
    path('profile/', profile_view, name='profile'),
    path('apply/<int:id>/', apply_scholarship, name='apply'),
]
