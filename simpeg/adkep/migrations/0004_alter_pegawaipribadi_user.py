# Generated by Django 4.2.1 on 2023-07-18 04:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('adkep', '0003_pegawaipribadi_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pegawaipribadi',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
