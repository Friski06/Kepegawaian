# Generated by Django 4.2.1 on 2023-08-07 14:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('perizinan', '0014_alter_cutiizin_jabatan'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cutiizin',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
