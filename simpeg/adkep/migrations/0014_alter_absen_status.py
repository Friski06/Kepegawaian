# Generated by Django 4.2.1 on 2023-05-09 06:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adkep', '0013_remove_absen_masuk_remove_absen_nama_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='absen',
            name='status',
            field=models.CharField(max_length=20),
        ),
    ]
