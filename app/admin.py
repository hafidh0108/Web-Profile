from django.contrib import admin
from . import models

# Register your models here.
admin.site.register(models.Saya)
admin.site.register(models.Pendidikan)
admin.site.register(models.Sertifikat)
admin.site.register(models.KategoriProjek)
admin.site.register(models.Projek)
admin.site.register(models.DokumentasiProjek)
admin.site.register(models.TeknologiProjek)
admin.site.register(models.Kemampuan)
admin.site.register(models.TingkatanKemampuan)
admin.site.register(models.Kerja)