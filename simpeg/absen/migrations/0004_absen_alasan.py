# Generated by Django 4.2.1 on 2023-05-29 14:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('absen', '0003_alter_absen_jabatanstruktural'),
    ]

    operations = [
        migrations.AddField(
            model_name='absen',
            name='alasan',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
