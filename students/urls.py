from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.student_dashboard, name='student_dashboard'),
    path('profile/create/', views.create_student_profile, name='create_student_profile'),
    path('profile/update/', views.update_student_profile, name='update_student_profile'),
    path('scholarships/', views.available_scholarships, name='available_scholarships'),
    path('scholarships/<int:scholarship_id>/apply/', views.apply_scholarship, name='apply_scholarship'),
    path('scholarships/<int:scholarship_id>/', views.scholarship_detail, name='scholarship_detail'),
    path('applications/', views.my_applications, name='my_applications'),
]