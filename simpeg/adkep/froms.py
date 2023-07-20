from django.forms import ModelForm
from django import forms
from adkep.models import JabatanStruktural, PegawaiPribadi, PegawaiPekerjaan, PegawaiPendidikan, PegawaiKeluarga, PegawaiBank, Provinsi, Kabupaten
from perizinan.models import  Jabatan

class JabatanForm(ModelForm):
    class Meta:
        model = Jabatan
        fields = '__all__'


class JabatanStrukturalForm(ModelForm):
    class Meta:
        model = JabatanStruktural
        fields = '__all__'

class ProvinsiForm(ModelForm):
    class Meta:
        model = Provinsi
        fields = '__all__'

class KabupatenForm(ModelForm):
    class Meta:
        model = Kabupaten
        fields = '__all__'

class PegawaiPribadiForm(ModelForm):
    JENIS_KELAMIN_CHOICES = [
        ('L', 'Laki-laki'),
        ('P', 'Perempuan')
    ]
    GOLONGAN_DARAH_CHOICES = [
        ('A', 'A'),
        ('B', 'B'),
        ('AB', 'AB'),
        ('O', 'O'),
    ]
    foto = forms.ImageField(required=False, widget=forms.ClearableFileInput(attrs={'class': 'form-control'}))
    nama = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    nrp_kontrak = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    nrp_tetap = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    nip = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    gelar = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    jenis_kelamin = forms.ChoiceField(choices=JENIS_KELAMIN_CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))
    tgl_lahir = forms.DateField(widget=forms.DateInput(attrs={'class': 'form-control','type': 'date'}))
    gol_darah = forms.ChoiceField(choices=GOLONGAN_DARAH_CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))
    agama = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    jalan = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}))
    nmr_rumah = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    provinsi = forms.ModelChoiceField(queryset=Provinsi.objects.all(), empty_label=None, widget=forms.Select(attrs={'class': 'form-control'}))
    kode_pos = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    desa = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}))
    kecamatan = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}))
    kabupaten = forms.ModelChoiceField(queryset=Kabupaten.objects.all(), empty_label=None, widget=forms.Select(attrs={'class': 'form-control'}))
    tlp_rumah = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    hp = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = PegawaiPribadi
        exclude = ['user', 'pekerjaan','pendidikan']
class PegawaiPekerjaanForm(ModelForm):
    
    PEGAWAI_CHOICES = [
        ('tetap', 'Pegawai Tetap'),
        ('honor', 'Pegawai Honor'),
        ('pns', 'Pegawai PNS'),
    ]
    STATUS_CHOICES = [
        ('aktif', 'Aktif'),
        ('keluar', 'Keluar'),
        ('resign', 'Resign'),
        ('tidak_aktif', 'Tidak Aktif'),
        ('tugas_belajar', 'Tugas Belajar'),
        ('izin_belajar', 'Izin Belajar'),
    ]
    POSISI_CHOICES = [
        ('dosen', 'Dosen'),
        ('staf', 'Staf'),
        ('administrasi', 'Administrasi'),
        ('pustakawan', 'Pustakawan'),
        ('teknisi', 'Teknisi'),
        ('rumah_tangga', 'Rumah Tangga')
    ]
    PRODI_CHOICES = [
        ('teknik elektronika industri', 'Teknik Elekronika Industri'),
        ('akutansi', 'Akutansi'),
        ('teknik informasi', 'Teknologi Informasi'),
        ('mekatronika', 'Mekatronika'),
        ('staf','Staf'),
       
    ]
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
    nama = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    nip = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    mulai_kerja = forms.DateField(widget=forms.DateInput(attrs={'class': 'form-control','type': 'date'}))
    lama_kerja = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    pegawai = forms.ChoiceField(choices=PEGAWAI_CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))
    status = forms.ChoiceField(choices=STATUS_CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))
    posisi = forms.ChoiceField(choices=POSISI_CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))
    unit = forms.ChoiceField(choices=UNIT_CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))
    program_studi = forms.ChoiceField(choices=PRODI_CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))
    berhenti_kerja = forms.DateField(widget=forms.DateInput(attrs={'class': 'form-control','type': 'date'}))
    alasan = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    tmt = forms.DateField(widget=forms.DateInput(attrs={'class': 'form-control','type': 'date'}))
    tst = forms.DateField(widget=forms.DateInput(attrs={'class': 'form-control','type': 'date'}))
    NIDN_NUP_NITL_NIDK = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    jabatan_fungsional = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    gol = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    sertifikasi_dosen = forms.ImageField(required=False, widget=forms.ClearableFileInput(attrs={'class': 'form-control'}))
    no_sertifikasi_dosen = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    jabatan = forms.ModelChoiceField(queryset=JabatanStruktural.objects.all(), empty_label=None, widget=forms.Select(attrs={'class': 'form-control'}))

    class Meta:
        model = PegawaiPekerjaan
        fields = '__all__'

class PegawaiPendidikanForm(ModelForm):
    nama = forms.ModelChoiceField(queryset=PegawaiPribadi.objects.all(), empty_label=None, widget=forms.Select(attrs={'class': 'form-control'}))
    nip = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    pendidikan_terakhir = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    perguruan = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    bidang= forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    sertifikat_keahlian = forms.ImageField(required=False, widget=forms.ClearableFileInput(attrs={'class': 'form-control'}))
    masa_berlaku = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    organisasi_profesi = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    kurun_waktu = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    tingkat = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    class Meta:
        model = PegawaiPendidikan
        exclude = ['pribadi']

class PegawaiKeluargaForm(ModelForm):
    JENIS_KELAMIN_CHOICES = [
        ('L', 'Laki-laki'),
        ('P', 'Perempuan'),
    ]
    nama = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    nip = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    nama_pasangan = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    tempat_lahir = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    tgl_lahir = forms.DateField(widget=forms.DateInput(attrs={'class': 'form-control','type': 'date'}))
    hp = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    anak1 = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    jk4 = forms.ChoiceField(choices=JENIS_KELAMIN_CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))
    tgl_lahir_a1 = forms.DateField(widget=forms.DateInput(attrs={'class': 'form-control','type': 'date'}), required=False)
    anak2 = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), required=False)
    tgl_lahir_a2 = forms.DateField(widget=forms.DateInput(attrs={'class': 'form-control','type': 'date'}), required=False)
    jk6 = forms.ChoiceField(choices=JENIS_KELAMIN_CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))
    anak3 = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), required=False)
    jk8 = forms.ChoiceField(choices=JENIS_KELAMIN_CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))
    tgl_lahir_a3 = forms.DateField(widget=forms.DateInput(attrs={'class': 'form-control','type': 'date'}), required=False)
    jumlah_anak = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), required=False)
    class Meta:
        model = PegawaiKeluarga
        fields = '__all__'

class PegawaiBankForm(ModelForm):
    nama = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    nip = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    no_rek_bank = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    nama_bank = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    cabang = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    atasnama = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    npwp = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    no_bpjs_tenagakerja = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    no_bpjs_kesehatan = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    class Meta:
        model = PegawaiBank
        fields = '__all__'


    