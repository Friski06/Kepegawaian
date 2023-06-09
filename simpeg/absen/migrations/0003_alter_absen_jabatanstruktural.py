# Generated by Django 4.2.1 on 2023-05-29 14:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('absen', '0002_remove_absen_rekap_bulan'),
    ]

    operations = [
        migrations.AlterField(
            model_name='absen',
            name='jabatanstruktural',
            field=models.CharField(choices=[('DIREKTUR', 'Direktur'), ('WADIR', 'Wakil Direktur'), ('KETUA_SPMI', 'Ketua SPMI'), ('KABAG_KA_UPT', 'Kabag/Ka. UPT'), ('KAPRODI', 'Kaprodi'), ('SEKPRODI', 'Sekretaris Prodi'), ('KA_LAB', 'Kepala Lab'), ('PENATA_LK', 'Penata LK'), ('BENDAHARA', 'Bendahara'), ('KA_UNIT', 'Kepala Unit'), ('SEKETARIS_DIREKTUR', 'Sekretaris Direktur'), ('OPERATOR_PT', 'Operator PT'), ('KEPALA_ASRAMA', 'Kepala Asrama'), ('DOSEN', 'Dosen'), ('STAF', 'Staf')], max_length=50),
        ),
    ]
