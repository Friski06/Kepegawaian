# Generated by Django 4.2.1 on 2023-08-25 17:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('perizinan', '0025_upload_spt_pegawaipribadi'),
    ]

    operations = [
        migrations.AddField(
            model_name='upload_spt',
            name='spt',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='perizinan.spt'),
        ),
    ]
