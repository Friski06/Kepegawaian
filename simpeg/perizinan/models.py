from django.db import models
from adkep.models import JabatanBawahan, PegawaiPribadi
from django.conf import settings
from django.utils import timezone
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
    
    
    keperluan = models.CharField(max_length=100)
    tgl_mulai = models.DateField()
    tgl_selesai = models.DateField()
    jabatan = models.ForeignKey(JabatanBawahan, on_delete=models.CASCADE,max_length=100, null=True)
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
    pegawaipribadi = models.ForeignKey(PegawaiPribadi, on_delete=models.CASCADE, null=True)

    def save(self, *args, **kwargs):
        # Calculate the duration between tgl_mulai and tgl_selesai
        if self.tgl_mulai and self.tgl_selesai:
            duration = self.tgl_selesai - self.tgl_mulai
            self.hari = duration.days + 1  # Add 1 to include both start and end dates

        super(Cutiizin, self).save(*args, **kwargs)

    def __str__(self):
        return f"cutiizin: {self.id}"
    

class Upload_Spt(models.Model):
    nama = models.CharField(max_length=200)
    pdf_file = models.FileField(upload_to='spt_pdfs/')
    pegawaipribadi = models.ForeignKey(PegawaiPribadi, on_delete=models.CASCADE, null=True)
    
   

    def __str__(self):
        return f"uploadspt: {self.id}"
        
class Spt(models.Model):
    STATUS = [
        ('BELUM', 'Belum Diverifikasi'),
        ('DISETUJUI', 'Disetujui'),
        ('DITOLAK', 'Ditolak'),
    ]
    pegawai_nama = models.CharField(max_length=100,null=True, blank=True)
    pegawai_nip = models.CharField(max_length=50,null=True, blank=True)
    jenis_kegiatan = models.CharField(max_length=100)
    tempat_kegiatan = models.CharField(max_length=100)
    tgl_mulai_kegiatan = models.DateField()
    tgl_selesai_kegiatan = models.DateField()
    status = models.CharField(max_length=20, choices=STATUS, default='BELUM')
    jabatan = models.ForeignKey(JabatanBawahan, on_delete=models.CASCADE,max_length=100, null=True)
    pegawaipribadi = models.ForeignKey(PegawaiPribadi, on_delete=models.CASCADE, null=True)
    spt = models.ForeignKey(Upload_Spt, on_delete=models.CASCADE, null=True)
    tanggal_pengajuan = models.DateField(default=timezone.now)
    
    def __str__(self):
        return f"spt: {self.id}"
    


class Notifikasi(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    isi_notifikasi = models.TextField()
    sudah_dibaca = models.BooleanField(default=False)
    tanggal_dibuat = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.isi_notifikasi