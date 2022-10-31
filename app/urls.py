from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.about, name='about'),
    path('education/', views.education, name='education'),
    path('skills/', views.skills, name='skills'),
    path('experience/', views.experience, name='experience'),
    path('portfolio/', views.portfolio, name='portfolio'),
    path('portfolio/detail/<uuid:pk>', views.portfolio_detail, name='portfolio_detail')
]

if settings.DEBUG:
   urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)