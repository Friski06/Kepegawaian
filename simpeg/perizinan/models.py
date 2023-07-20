from django.db import models

# Create your models here.

class Jabatan(models.Model):
    nama = models.CharField(max_length=255)
    def __str__(self):
     return self.nama

class Cutiizin(models.Model):
    UNIT_CHOICES = [
        ('pengembangan_akademik', 'Pengembangan Akademik'),
        ('pengembangan_kemahasiswaan', 'Pengembangan Kemahasiswaan'),
        ('pusat_penelitian_dan_pengabdian_masyarakat', 'Pusat Penelitian Dan Pengabdian Masyarakat'),
        ('program_studi', 'Program Studi'),
        ('keuangan', 'Keuangan'),
        ('kepegawaian', 'Kepegawaian'),
        ('kerjasama_dan_humas', 'Kerjasama Dan Humas'),
        ('pusat_inkubasi_bisnis', 'Pusat Inkubasi Bisnis'),
        ('pusat_perencanaan_dan_pengembangan', 'Pusat Perencanaan Dan Pengembangan'),
        ('pusat_data_dan_akreditasi', 'Pusat Data Dan Akreditasi'),
        ('pusat_pengawasan_pengadilan_internal', 'Pusat Pengawasan Pengadilan Internal'),
    ]
    verifikasi_choices = [
        ('BELUM', 'Belum Diverifikasi'),
        ('DISETUJUI', 'Disetujui'),
        ('DITOLAK', 'Ditolak'),
    ]
    nama = models.CharField(max_length=40)
    nrp = models.IntegerField(null=True)
    keperluan = models.CharField(max_length=100)
    tgl_mulai = models.DateField()
    tgl_selesai = models.DateField()
    jabatan = models.CharField(max_length=255, null=True)
    unit = models.CharField(choices=UNIT_CHOICES, max_length=100, null=True)
    jam_mulai = models.TimeField(null=True)
    jam_selesai = models.TimeField(null=True)
    hari = models.CharField(max_length=20,null=True)
    jam = models.TimeField(null=True)
    ka_unit = models.CharField(max_length=20,null=True)
    direksi = models.CharField(max_length=20, null=True)
    verifikasi_kaunit = models.CharField(max_length=20, choices=verifikasi_choices, default='BELUM')
    verifikasi_direksi = models.CharField(max_length=20, choices=verifikasi_choices, default='BELUM')
    verifikasi_status = models.CharField(max_length=20, choices=verifikasi_choices, default='BELUM')


    
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
    
