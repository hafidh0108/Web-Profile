from django.db import models

# Create your models here.
class Saya(models.Model):
    nama = models.CharField(max_length=50)
    email = models.CharField(max_length=30)
    no_hp = models.CharField(max_length=15, null=True)
    tempat_lahir = models.CharField(max_length=20)
    tanggal_lahir = models.CharField(max_length=20)
    alamat = models.TextField()
    deskripsi = models.TextField()

    def __str__(self):
        return self.nama
    
class Pendidikan(models.Model):
    institusi = models.CharField(max_length=30)
    tahun_mulai = models.CharField(max_length=10)
    tahun_selesai = models.CharField(max_length=10)
    jurusan = models.CharField(max_length=30, null=True)
    jenjang = models.CharField(max_length=30, null=True)
    deskripsi = models.TextField(null=True)

    def __str__(self):
        return self.institusi
    
class Sertifikat(models.Model):
    sertifikat = models.CharField(max_length=50)
    scan = models.ImageField(upload_to='scan/')

    def __str__(self):
        return self.sertifikat

class KategoriProjek(models.Model):
    kategori_projek = models.CharField(max_length=30)

    def __str__(self):
        return self.kategori
    
class Projek(models.Model):
    nama_projek = models.CharField(max_length=100)
    kategori_projek = models.ForeignKey('app.KategoriProjek', on_delete=models.CASCADE)
    posisi = models.CharField(max_length=30)
    link = models.CharField(max_length=200, null=True)
    
class DokumentasiProjek(models.Model):
    projek = models.ForeignKey(Projek, on_delete=models.CASCADE)
    nama_dokumentasi = models.CharField(max_length=100)
    gambar = models.ImageField(upload_to='projek/')
    deskripsi_dokumentasi = models.TextField()
    
    def __str__(self):
        return self.nama_dokumentasi
    
class TeknologiProjek(models.Model):
    projek = models.ForeignKey(Projek, on_delete=models.CASCADE)
    teknologi = models.CharField(max_length=50)

    def __str__(self):
        return self.teknologi
    
class Kemampuan(models.Model):
    kemampuan = models.CharField(max_length=50)
    logo = models.ImageField(upload_to='logo/')
    tingkatan = models.ForeignKey('app.TingkatanKemampuan', on_delete=models.CASCADE)

    def __str__(self):
        return self.kemampuan
    
class TingakatanKemampuan(models.Model):
    tingkatan = models.CharField(max_length=255)
    
    def __str__(self):
        return self.tingkatan