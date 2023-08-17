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
    
    tempat_tgl_lahir = models.CharField(max_length=50)
    pangkat_gol_ruang_tmt = models.CharField(max_length=50)
    tanggal = models.DateField()
    masuk = models.TimeField()
    pulang = models.TimeField()
    jumlah_jam = models.DecimalField(max_digits=5, decimal_places=2)
    jumlah_potongan_tukin = models.DecimalField(max_digits=5, decimal_places=2)
    jabatan = models.ForeignKey(JabatanBawahan, on_delete=models.CASCADE,null=True)
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
    unit = models.CharField(choices=UNIT_CHOICES, max_length=100)
    PRODI_CHOICES = [
        ('teknik elektronika industri', 'Teknik Elekronika Industri'),
        ('akutansi', 'Akutansi'),
        ('teknik informasi', 'Teknologi Informasi'),
        ('mekatronika', 'Mekatronika'),
    ]
    program_studi = models.CharField(choices=PRODI_CHOICES, max_length=30)
    alasan = models.CharField(max_length=100, blank=True)
    
    status = models.CharField(max_length=20, choices=STATUS, default='BELUM')
    pegawaipribadi = models.ForeignKey(PegawaiPribadi, on_delete=models.CASCADE, null=True)

    def rekap_absen_perbulan(cls, bulan, tahun):
        return cls.objects.filter(tanggal__month=bulan, tanggal__year=tahun)

    def __str__(self):
        return f"Absen: {self.id} - {self.tanggal}"