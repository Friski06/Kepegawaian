# Generated by Django 4.2.1 on 2023-08-06 13:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0005_user_jabatan'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='jabatan',
        ),
    ]