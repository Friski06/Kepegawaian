# Generated by Django 4.2.1 on 2023-05-09 05:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('adkep', '0012_alter_absen_nama_alter_absen_nrp'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='absen',
            name='masuk',
        ),
        migrations.RemoveField(
            model_name='absen',
            name='nama',
        ),
        migrations.RemoveField(
            model_name='absen',
            name='nrp',
        ),
        migrations.RemoveField(
            model_name='absen',
            name='pulang',
        ),
    ]