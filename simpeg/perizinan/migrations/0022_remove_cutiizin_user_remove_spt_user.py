# Generated by Django 4.2.1 on 2023-08-22 14:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('perizinan', '0021_remove_cutiizin_nama_remove_cutiizin_nrp_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cutiizin',
            name='user',
        ),
        migrations.RemoveField(
            model_name='spt',
            name='user',
        ),
    ]
