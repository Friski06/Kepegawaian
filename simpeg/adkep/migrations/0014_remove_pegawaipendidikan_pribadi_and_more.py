# Generated by Django 4.2.1 on 2023-07-20 08:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('adkep', '0013_pegawaipendidikan_pribadi'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pegawaipendidikan',
            name='pribadi',
        ),
        migrations.AddField(
            model_name='pegawaipribadi',
            name='pendidikan',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='adkep.pegawaipendidikan'),
        ),
        migrations.AlterField(
            model_name='pegawaipribadi',
            name='pekerjaan',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='adkep.pegawaipekerjaan'),
        ),
    ]