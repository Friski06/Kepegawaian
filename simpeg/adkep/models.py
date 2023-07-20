from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
# Create your models here.

class JabatanStruktural(models.Model):
    
    nama_jabatan = models.CharField(max_length=100)
    id_atasan = models.CharField(max_length=20, blank=True)
    id_bawahan = models.CharField(max_length=100,blank=True)
    
    def __str__(self):
        return self.nama_jabatan
    
#atasan

# provinsi
class Provinsi(models.Model):
    nama_provinsi = models.CharField(max_length=255)

    def __str__(self):
        return self.nama_provinsi

#kabupaten
class Kabupaten(models.Model):
    nama_kabupaten = models.CharField(max_length=255)
    provinsi_id = models.ForeignKey(Provinsi, on_delete=models.CASCADE, null=True)
    def __str__(self):
        return self.nama_kabupaten


 #pekerjaan
class PegawaiPekerjaan(models.Model):
    nama = models.CharField(max_length=40, null=True)
    nip = models.CharField(max_length=20,null= True)
    mulai_kerja = models.DateField()
    lama_kerja = models.IntegerField()
    PEGAWAI_CHOICES = [
        ('tetap', 'Pegawai Tetap'),
        ('honor', 'Pegawai Honor'),
        ('pns', 'Pegawai PNS'),
    ]
    pegawai = models.CharField(choices=PEGAWAI_CHOICES, max_length=10)
    STATUS_CHOICES = [
        ('aktif', 'Aktif'),
        ('keluar', 'Keluar'),
        ('resign', 'Resign'),
        ('tidak_aktif', 'Tidak Aktif'),
        ('tugas_belajar', 'Tugas Belajar'),
        ('izin_belajar', 'Izin Belajar'),
    ]
    status = models.CharField(choices=STATUS_CHOICES, max_length=15)
    POSISI_CHOICES = [
        ('dosen', 'Dosen'),
        ('staf', 'Staf'),
        ('administrasi', 'Administrasi'),
        ('pustakawan', 'Pustakawan'),
        ('teknisi', 'Teknisi'),
        ('rumah_tangga', 'Rumah Tangga'),
    ]
    posisi = models.CharField(choices=POSISI_CHOICES, max_length=15)
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
        ('STAF', 'Staf')
    ]
    program_studi = models.CharField(choices=PRODI_CHOICES, max_length=30)
    berhenti_kerja = models.DateField(null=True, blank=True)
    alasan = models.CharField(max_length=100, null=True, blank=True)
    tmt = models.DateField(null=True, blank=True)
    tst = models.DateField(null=True, blank=True)
    NIDN_NUP_NITL_NIDK = models.CharField(max_length=20, null=True, blank=True)
    jabatan_fungsional = models.CharField(max_length=50, null=True, blank=True)
    gol = models.CharField(max_length=10, null=True, blank=True)
    sertifikasi_dosen = models.ImageField(upload_to='pegawaipekerjaan/', null=True, blank=True)
    no_sertifikasi_dosen = models.CharField(max_length=20, null=True, blank=True)
    jabatan = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return f"Pegawai Pekerjaan: {self.id}"
    
#pendidikan
class PegawaiPendidikan(models.Model):
    nama = models.CharField(max_length=40,null=True)
    nip = models.CharField(max_length=20, null=True)
    pendidikan_terakhir = models.CharField(max_length=50)
    perguruan = models.CharField(max_length=100, null=True, blank=True)
    bidang = models.CharField(max_length=100, null=True, blank=True)
    sertifikat_keahlian = models.ImageField(upload_to='pegawaipendidikan/', null=True, blank=True)
    masa_berlaku = models.DateField(null=True, blank=True)
    organisasi_profesi = models.CharField(max_length=100, null=True, blank=True)
    kurun_waktu = models.CharField(max_length=100, null=True, blank=True)
    tingkat = models.CharField(max_length=100, null=True, blank=True)
    
    def __str__(self):
        return f"Pegawai Pendidikan: {self.id}"
    
#keluarga
class PegawaiKeluarga(models.Model):
    nama = models.CharField(max_length=40, null=True)
    nip = models.CharField(max_length=20,null=True)
    nama_pasangan = models.CharField(max_length=40, null=True, blank=True)
    tempat_lahir = models.CharField(max_length=50, null=True, blank=True)
    tgl_lahir = models.DateField(null=True, blank=True)
    hp = models.CharField(max_length=20, null=True, blank=True)
    anak1 = models.CharField(max_length=40, null=True, blank=True)
    JENIS_KELAMIN_CHOICES = [
        ('L', 'Laki-laki'),
        ('P', 'Perempuan'),
    ]
    jk4 = models.CharField(choices=JENIS_KELAMIN_CHOICES, max_length=1, null=True, blank=True)
    tgl_lahir_a1 = models.DateField(null=True, blank=True)
    anak2 = models.CharField(max_length=40, null=True, blank=True)
    tgl_lahir_a2 = models.DateField(null=True, blank=True)
    jk6 = models.CharField(choices=JENIS_KELAMIN_CHOICES, max_length=1, null=True, blank=True)
    anak3 = models.CharField(max_length=40, null=True, blank=True)
    jk8 = models.CharField(choices=JENIS_KELAMIN_CHOICES, max_length=1, null=True, blank=True)
    tgl_lahir_a3 = models.DateField(null=True, blank=True)
    jumlah_anak = models.PositiveIntegerField(null=True, blank=True)
    
    def __str__(self):
        return f"Pegawai Keluarga: {self.id}"
    
#bank
class PegawaiBank(models.Model):
    nama = models.CharField(max_length=40, null=True)
    nip = models.CharField(max_length=20, null=True)
    no_rek_bank = models.CharField(max_length=20, null=True, blank=True)
    nama_bank = models.CharField(max_length=50, null=True, blank=True)
    cabang = models.CharField(max_length=50, null=True, blank=True)
    atasnama = models.CharField(max_length=50, null=True, blank=True)
    npwp = models.CharField(max_length=20, null=True, blank=True)
    no_bpjs_tenagakerja = models.CharField(max_length=20, null=True, blank=True)
    no_bpjs_kesehatan = models.CharField(max_length=20, null=True, blank=True)

    def __str__(self):
        return f"Pegawai Bank: {self.id}" 

#pribadi
class PegawaiPribadi(models.Model):
    foto = models.ImageField(upload_to='pegawai/', null=True, blank=True)
    nama = models.CharField(max_length=40)
    nrp_kontrak = models.CharField(max_length=20)
    nrp_tetap = models.CharField(max_length=20)
    nip = models.CharField(max_length=20)
    gelar = models.CharField(max_length=20)
    JENIS_KELAMIN_CHOICES = [
        ('L', 'Laki-laki'),
        ('P', 'Perempuan'),
    ]
    jenis_kelamin = models.CharField(choices=JENIS_KELAMIN_CHOICES, max_length=1)
    tgl_lahir = models.DateField()
    GOLONGAN_DARAH_CHOICES = [
        ('A', 'A'),
        ('B', 'B'),
        ('AB', 'AB'),
        ('O', 'O'),
    ]
    gol_darah = models.CharField(choices=GOLONGAN_DARAH_CHOICES, max_length=2)
    agama = models.CharField(max_length=20)
    jalan = models.CharField(max_length=50)
    nmr_rumah = models.CharField(max_length=10)
    desa = models.CharField(max_length=50)
    kecamatan = models.CharField(max_length=50)
    kabupaten = models.CharField(max_length=50)
    provinsi = models.CharField(max_length=50)
    kode_pos = models.CharField(max_length=10)
    tlp_rumah = models.CharField(max_length=20)
    hp = models.CharField(max_length=20)
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,primary_key=True)
    pekerjaan = models.ForeignKey(PegawaiPekerjaan, on_delete=models.CASCADE, null=True, blank=True)
    pendidikan = models.ForeignKey(PegawaiPendidikan, on_delete=models.CASCADE, null=True, blank=True)
    
    def __str__(self):
        return self.nama

    
