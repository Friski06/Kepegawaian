# Generated by Django 4.2.1 on 2023-08-25 16:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('perizinan', '0023_spt_pegawai_nama_spt_pegawai_nip'),
    ]

    operations = [
        migrations.CreateModel(
            name='Upload_Spt',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=200)),
                ('pdf_file', models.FileField(upload_to='spt_pdfs/')),
            ],
        ),
    ]
