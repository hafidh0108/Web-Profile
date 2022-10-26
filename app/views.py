from django.shortcuts import render
from . import models

# Create your views here.
def about(request):
    saya = models.Saya.objects.all()
    konteks = {
        'saya' : saya,
    }
    return render(request, 'about.html', konteks)

def education(request):
    pendidikan = models.Pendidikan.objects.all()
    konteks = {
        'pendidikan' : pendidikan
    }
    return render(request, 'education.html', konteks)