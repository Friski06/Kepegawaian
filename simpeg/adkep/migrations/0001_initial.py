# Generated by Django 4.2.1 on 2023-05-06 16:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pegawai',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=40)),
                ('email', models.CharField(max_length=40)),
                ('alamat', models.CharField(max_length=50)),
            ],
        ),
    ]