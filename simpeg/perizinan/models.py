from django.db import models

# Create your models here.

class Cutiizin(models.Model):
    nama = models.CharField(max_length=40)
    nrp = models.IntegerField(null=True)
    jabatan = models.CharField(max_length=40, null=True)
    keperluan = models.CharField(max_length=100)
    tgl_mulai = models.DateField()
    tgl_selesai = models.DateField()
    
    
    def __str__(self):
        return self.nama

class Spt(models.Model):
    nama = models.CharField(max_length=40)
    nrp = models.IntegerField(null=True)
    jenis_kegiatan = models.CharField(max_length=100)
    tempat_kegiatan = models.CharField(max_length=100)
    tgl_mulai_kegiatan = models.DateField()
    tgl_selesai_kegiatan = models.DateField()
    
    
    def __str__(self):
        return self.nama