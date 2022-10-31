from django.db import models
import uuid

# Create your models here.
class Saya(models.Model):
    nama = models.CharField(max_length=255)
    email = models.CharField(max_length=30)
    no_hp = models.CharField(max_length=15, null=True)
    tempat_lahir = models.CharField(max_length=20)
    tanggal_lahir = models.CharField(max_length=20)
    alamat = models.TextField()
    deskripsi = models.TextField()
    linkedin = models.CharField(max_length=255, null=True)
    github = models.CharField(max_length=255, null=True)
    twitter = models.CharField(max_length=255, null=True)
    instagram = models.CharField(max_length=255, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.nama
    
class Pendidikan(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    institusi = models.CharField(max_length=255)
    tahun_mulai = models.CharField(max_length=10)
    tahun_selesai = models.CharField(max_length=10)
    jurusan = models.CharField(max_length=30, null=True)
    jenjang = models.CharField(max_length=30, null=True)
    deskripsi = models.TextField(null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.institusi
    
class Sertifikat(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    sertifikat = models.CharField(max_length=255)
    scan = models.ImageField(upload_to='scan/')
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.sertifikat

class KategoriProjek(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    kategori_projek = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.kategori_projek
    
class Projek(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nama_projek = models.CharField(max_length=255)
    kategori_projek = models.ForeignKey('app.KategoriProjek', on_delete=models.CASCADE)
    posisi = models.ForeignKey('app.PosisiProjek', on_delete=models.CASCADE)
    link = models.CharField(max_length=200, null=True , blank=True)
    deskripsi = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    
    def __str__(self):
        return self.nama_projek
    
class DokumentasiProjek(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    projek = models.ForeignKey(Projek, on_delete=models.CASCADE, related_name='dokumentasi_projek')
    nama_dokumentasi = models.CharField(max_length=255)
    gambar = models.ImageField(upload_to='projek/')
    deskripsi_dokumentasi = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    
    def __str__(self):
        return self.nama_dokumentasi
    
class TeknologiProjek(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    projek = models.ForeignKey('app.Projek', on_delete=models.CASCADE, related_name='teknologi_projek')
    teknologi = models.ForeignKey('app.Teknologi', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return f'{self.teknologi} | {self.projek.nama_projek}'
    
class Kemampuan(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    kemampuan = models.CharField(max_length=255)
    logo = models.ImageField(upload_to='logo/', blank=True, null=True)
    tingkatan = models.ForeignKey('app.TingkatanKemampuan', on_delete=models.CASCADE, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    
    def __str__(self):
        return self.kemampuan
    
class TingkatanKemampuan(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    tingkatan = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    
    def __str__(self):
        return self.tingkatan
    
class Kerja(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    perusahaan = models.CharField(max_length=255)
    tahun_mulai = models.CharField(max_length=255)
    tahun_selesai = models.CharField(max_length=255)
    posisi = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    
    def __str__(self):
        return self.perusahaan
    
class TugasKerja(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    kerja = models.ForeignKey('app.Kerja', on_delete=models.CASCADE, related_name='tugas_kerja')
    tugas = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    
    def __str__(self):
        return self.tugas
    
class PosisiProjek(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    posisi = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.posisi
    
class Aktifitas(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    menu = models.CharField(max_length=255)
    diakses = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f'{self.menu} | {self.diakses}'
    
class Teknologi(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    teknologi = models.CharField(max_length=255)
    
    def __str__(self):
        return self.teknologi