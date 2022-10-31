from django.http import HttpResponseNotFound
from django.shortcuts import render
from . import models

# Create your views here.
def about(request):
    saya = models.Saya.objects.all()
    konteks = {
        'saya' : saya,
    }
    activity('about')
    return render(request, 'about.html', konteks)

def education(request):
    pendidikan = models.Pendidikan.objects.all().order_by('-tahun_mulai')
    konteks = {
        'pendidikan' : pendidikan
    }
    activity('education')
    return render(request, 'education.html', konteks)

def skills(request):
    kemampuan = models.Kemampuan.objects.all()
    konteks = {
        'kemampuan' : kemampuan
    }
    activity('skills')
    return render(request, 'skills.html', konteks)

def experience(request):
    kerja = models.Kerja.objects.all()
    konteks = {
        'kerja' : kerja,
    }
    activity('experience')
    return render(request, 'experience.html', konteks)

def portfolio(request):
    projek = models.Projek.objects.all().order_by('-created_at')
    konteks = {
        'projek' : projek
    }
    activity('portofolio')
    return render(request, 'portfolio.html', konteks)

def portfolio_detail(request, pk):
    try:
        projek = models.Projek.objects.get(id=pk)
        konteks = {
            'projek' : projek
        }
        return render(request, 'portfolio_detail.html', konteks)
    except models.Projek.DoesNotExist:
        return HttpResponseNotFound('')

def activity(menu):
    models.Aktifitas.objects.create(menu=menu)