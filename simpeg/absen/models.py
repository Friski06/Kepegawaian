from django.db import models
from adkep.models import JabatanBawahan, PegawaiPribadi
from django.conf import settings

# Create your models here.

class Absen(models.Model):
    STATUS = [
        ('BELUM', 'Belum Diverifikasi'),
        ('DISETUJUI', 'Disetujui'),
        ('DITOLAK', 'Ditolak'),
    ]
    tanggal = models.DateField()
    masuk = models.TimeField()
    pulang = models.TimeField()
    jumlah_jam = models.DecimalField(max_digits=5, decimal_places=2)
    jumlah_potongan_tukin = models.DecimalField(max_digits=5, decimal_places=2)
    jabatan = models.ForeignKey(JabatanBawahan, on_delete=models.CASCADE,null=True)
    alasan = models.CharField(max_length=100, blank=True)
    status = models.CharField(max_length=20, choices=STATUS, default='BELUM')
    pegawaipribadi = models.ForeignKey(PegawaiPribadi, on_delete=models.CASCADE, null=True)

    def rekap_absen_perbulan(cls, bulan, tahun):
        return cls.objects.filter(tanggal__month=bulan, tanggal__year=tahun)

    def __str__(self):
        return f"Absen: {self.id} - {self.tanggal}"