# Generated by Django 4.2.1 on 2023-05-09 05:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adkep', '0011_alter_absen_masuk_alter_absen_pulang'),
    ]

    operations = [
        migrations.AlterField(
            model_name='absen',
            name='nama',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='absen',
            name='nrp',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
