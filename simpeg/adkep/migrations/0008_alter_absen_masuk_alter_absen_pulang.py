# Generated by Django 4.2.1 on 2023-05-08 23:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adkep', '0007_rename_status_pegawai_absen_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='absen',
            name='masuk',
            field=models.TimeField(null=True),
        ),
        migrations.AlterField(
            model_name='absen',
            name='pulang',
            field=models.TimeField(null=True),
        ),
    ]
