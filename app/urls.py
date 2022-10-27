from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.about, name='about'),
    path('education/', views.education, name='education'),
    path('skills/', views.skills, name='skills'),
    path('experience/', views.experience, name='experience')
]
