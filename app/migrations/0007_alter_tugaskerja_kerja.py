# Generated by Django 4.1.2 on 2022-10-26 07:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_remove_kerja_deskripsi_tugaskerja'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tugaskerja',
            name='kerja',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tugas_kerja', to='app.kerja'),
        ),
    ]
