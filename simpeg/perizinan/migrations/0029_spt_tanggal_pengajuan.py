# Generated by Django 4.2.1 on 2023-09-07 04:10

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('perizinan', '0028_alter_spt_pegawai_nama_alter_spt_pegawai_nip'),
    ]

    operations = [
        migrations.AddField(
            model_name='spt',
            name='tanggal_pengajuan',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]