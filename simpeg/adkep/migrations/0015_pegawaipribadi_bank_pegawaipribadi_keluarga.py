# Generated by Django 4.2.1 on 2023-07-22 07:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('adkep', '0014_remove_pegawaipendidikan_pribadi_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='pegawaipribadi',
            name='bank',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='adkep.pegawaibank'),
        ),
        migrations.AddField(
            model_name='pegawaipribadi',
            name='keluarga',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='adkep.pegawaikeluarga'),
        ),
    ]