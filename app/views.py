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

def experience(request):
    kerja = models.Kerja.objects.all()
    konteks = {
        'kerja' : kerja,
    }
    return render(request, 'experience.html', konteks)

def portfolio(request):
    projek = models.Projek.objects.all()
    konteks = {
        'projek' : projek
    }
    return render(request, 'portfolio.html', konteks)