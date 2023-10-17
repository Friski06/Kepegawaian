# Generated by Django 4.2.1 on 2023-08-28 16:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adkep', '0018_alter_pegawaipekerjaan_jabatan'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pegawaikeluarga',
            name='anak1',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='pegawaikeluarga',
            name='anak2',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='pegawaikeluarga',
            name='anak3',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='pegawaikeluarga',
            name='jk4',
            field=models.CharField(blank=True, choices=[('L', 'Laki-laki'), ('P', 'Perempuan')], max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='pegawaikeluarga',
            name='jk6',
            field=models.CharField(blank=True, choices=[('L', 'Laki-laki'), ('P', 'Perempuan')], max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='pegawaikeluarga',
            name='jk8',
            field=models.CharField(blank=True, choices=[('L', 'Laki-laki'), ('P', 'Perempuan')], max_length=10, null=True),
        ),
    ]
