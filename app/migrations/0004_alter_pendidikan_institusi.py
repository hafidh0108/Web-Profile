# Generated by Django 4.1.2 on 2022-10-26 06:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_kerja'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pendidikan',
            name='institusi',
            field=models.CharField(max_length=255),
        ),
    ]