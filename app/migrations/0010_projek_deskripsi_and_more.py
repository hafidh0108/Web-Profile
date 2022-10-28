# Generated by Django 4.1.2 on 2022-10-28 01:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_dokumentasiprojek_created_at_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='projek',
            name='deskripsi',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='dokumentasiprojek',
            name='nama_dokumentasi',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='kategoriprojek',
            name='kategori_projek',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='kemampuan',
            name='kemampuan',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='projek',
            name='link',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='projek',
            name='nama_projek',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='saya',
            name='nama',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='sertifikat',
            name='sertifikat',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='teknologiprojek',
            name='teknologi',
            field=models.CharField(max_length=255),
        ),
    ]
