# Generated by Django 4.2.1 on 2023-05-09 13:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('perizinan', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='spt',
            name='tempat_kegiatan',
            field=models.CharField(max_length=100),
        ),
    ]
