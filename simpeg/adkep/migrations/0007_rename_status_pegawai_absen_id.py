# Generated by Django 4.2.1 on 2023-05-07 16:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('adkep', '0006_pegawai_jabatan'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pegawai',
            old_name='status',
            new_name='absen_id',
        ),
    ]