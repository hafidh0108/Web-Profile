from django.urls import path, include
from . import views

urlpatterns = [
    path('about/', views.about, name='about'),
    path('education/', views.education, name='education'),
]
