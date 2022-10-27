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
    tugas_kerja = models.TugasKerja.objects.all()
    konteks = {
        'kerja' : kerja,
        'tugas_kerja' : tugas_kerja,
    }
    return render(request, 'experience.html', konteks)