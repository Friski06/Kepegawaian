# Generated by Django 4.2.1 on 2023-08-11 17:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('adkep', '0018_alter_pegawaipekerjaan_jabatan'),
        ('perizinan', '0018_spt_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='spt',
            name='jabatan',
            field=models.ForeignKey(max_length=100, null=True, on_delete=django.db.models.deletion.CASCADE, to='adkep.jabatanbawahan'),
        ),
    ]
