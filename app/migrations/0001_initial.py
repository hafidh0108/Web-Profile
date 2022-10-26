# Generated by Django 4.1.2 on 2022-10-26 04:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='KategoriProjek',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kategori_projek', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Pendidikan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('institusi', models.CharField(max_length=30)),
                ('tahun_mulai', models.CharField(max_length=10)),
                ('tahun_selesai', models.CharField(max_length=10)),
                ('jurusan', models.CharField(max_length=30, null=True)),
                ('jenjang', models.CharField(max_length=30, null=True)),
                ('deskripsi', models.TextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Projek',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama_projek', models.CharField(max_length=100)),
                ('posisi', models.CharField(max_length=30)),
                ('link', models.CharField(max_length=200, null=True)),
                ('kategori_projek', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.kategoriprojek')),
            ],
        ),
        migrations.CreateModel(
            name='Saya',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=30)),
                ('no_hp', models.CharField(max_length=15, null=True)),
                ('tempat_lahir', models.CharField(max_length=20)),
                ('tanggal_lahir', models.CharField(max_length=20)),
                ('alamat', models.TextField()),
                ('deskripsi', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Sertifikat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sertifikat', models.CharField(max_length=50)),
                ('scan', models.ImageField(upload_to='scan/')),
            ],
        ),
        migrations.CreateModel(
            name='TingkatanKemampuan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tingkatan', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='TeknologiProjek',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('teknologi', models.CharField(max_length=50)),
                ('projek', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.projek')),
            ],
        ),
        migrations.CreateModel(
            name='Kemampuan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kemampuan', models.CharField(max_length=50)),
                ('logo', models.ImageField(upload_to='logo/')),
                ('tingkatan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.tingkatankemampuan')),
            ],
        ),
        migrations.CreateModel(
            name='DokumentasiProjek',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama_dokumentasi', models.CharField(max_length=100)),
                ('gambar', models.ImageField(upload_to='projek/')),
                ('deskripsi_dokumentasi', models.TextField()),
                ('projek', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.projek')),
            ],
        ),
    ]