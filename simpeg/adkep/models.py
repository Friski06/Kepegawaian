from django.db import models

# Create your models here.

class Absen(models.Model):
    status = models.CharField(max_length=20)
    keterangan = models.CharField(max_length=100)
    
    
    def __str__(self):
        return self.status

class Pegawai(models.Model):
    nama = models.CharField(max_length=40)
    nrp = models.IntegerField(null=True)
    email = models.CharField(max_length=40)
    hp = models.IntegerField(null=True)
    alamat = models.CharField(max_length=50)
    jabatan = models.CharField(max_length=40, null=True)
    absen_id = models.ForeignKey(Absen, on_delete= models.CASCADE, null=True)
    

    def __str__(self):
        return self.nama