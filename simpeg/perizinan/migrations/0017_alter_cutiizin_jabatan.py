# Generated by Django 4.2.1 on 2023-08-07 14:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('adkep', '0018_alter_pegawaipekerjaan_jabatan'),
        ('perizinan', '0016_alter_cutiizin_jabatan'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cutiizin',
            name='jabatan',
            field=models.ForeignKey(max_length=100, null=True, on_delete=django.db.models.deletion.CASCADE, to='adkep.jabatanbawahan'),
        ),
    ]
