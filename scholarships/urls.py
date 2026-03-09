from django.urls import path
from . import views

urlpatterns = [
    path('', views.scholarship_list, name='scholarship_list'),
    path('<int:pk>/', views.scholarship_detail, name='scholarship_detail'),
]
