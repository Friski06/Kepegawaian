from django.db import models
from adkep.models import PegawaiPribadi
from django.utils import timezone

# Create your models here.

class Nilai(models.Model):
    kerapian = models.CharField(max_length=100)
    kesopanan = models.CharField(max_length=100)
    dedikasi = models.CharField(max_length=100)
    loyalitas = models.CharField(max_length=100)
    disiplin = models.CharField(max_length=100)
    kerjasama = models.CharField(max_length=100)
    tupoksi = models.CharField(max_length=100)
    rata_rata = models.CharField(max_length=100)
    nilai_huruf = models.CharField(max_length=100)
    potongan = models.CharField(max_length=100)
    pegawaipribadi = models.ForeignKey(PegawaiPribadi, on_delete=models.CASCADE, null=True)
    tanggal_penilaian = models.DateField(default=timezone.now)
    
    def __str__(self):
        return f"nilai: {self.id}"