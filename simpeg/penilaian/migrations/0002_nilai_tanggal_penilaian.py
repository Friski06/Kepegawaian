# Generated by Django 4.2.1 on 2023-08-23 11:27

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('penilaian', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='nilai',
            name='tanggal_penilaian',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
