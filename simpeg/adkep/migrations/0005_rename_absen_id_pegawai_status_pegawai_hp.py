# Generated by Django 4.2.1 on 2023-05-07 16:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adkep', '0004_absen_masuk_absen_pulang'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pegawai',
            old_name='absen_id',
            new_name='status',
        ),
        migrations.AddField(
            model_name='pegawai',
            name='hp',
            field=models.IntegerField(null=True),
        ),
    ]
