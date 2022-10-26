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
    pendidikan = models.Pendidikan.objects.all().order_by('-tahun_mulai')
    konteks = {
        'pendidikan' : pendidikan
    }
    return render(request, 'education.html', konteks)

def skills(request):
    kemampuan = models.Kemampuan.objects.all()
    konteks = {
        'kemampuan' : kemampuan
    }
    return render(request, 'skills.html', konteks)