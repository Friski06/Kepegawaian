from django.forms import ModelForm
from perizinan.models import Cutiizin, Spt, Jabatan, Upload_Spt
from django import forms
from adkep.models import JabatanBawahan

class JabatanBawahanForm(ModelForm):
    class Meta:
        model = JabatanBawahan
        fields = '__all__'
        

class FromCuti(forms.ModelForm):
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
    unit = forms.ChoiceField(choices=UNIT_CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))
    jabatan = forms.ModelChoiceField(queryset=JabatanBawahan.objects.all(), empty_label=None, widget=forms.Select(attrs={'class': 'form-control'}))
    class Meta:
        model = Cutiizin
        fields = [ 'tgl_mulai', 'tgl_selesai', 'jam_mulai', 'jam_selesai','jabatan', 'unit', 'hari', 'jam','keperluan']
        exclude = ['hari']
        widgets = {
            
            
            'tgl_mulai': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'tgl_selesai': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'jam_mulai': forms.TimeInput(attrs={'class': 'form-control', 'type': 'time'}),
            'jam_selesai': forms.TimeInput(attrs={'class': 'form-control', 'type': 'time'}),
            'hari': forms.TextInput(attrs={'class': 'form-control','readonly': 'readonly'}),
            'jam': forms.TimeInput(attrs={'class': 'form-control'}),
            'ka_unit': forms.Select(attrs={'class': 'form-control'}),
            'direksi': forms.Select(attrs={'class': 'form-control'}),
            'keperluan': forms.Textarea(attrs={'class': 'form-control'}),
        }

class VerifikasiForm(forms.ModelForm):
    class Meta:
        model = Cutiizin
        fields = ['verifikasi_kaunit', 'verifikasi_direksi']

class FromSpt(ModelForm):
    jabatan = forms.ModelChoiceField(queryset=JabatanBawahan.objects.all(), empty_label=None, widget=forms.Select(attrs={'class': 'form-control'}))
    class Meta:
        model = Spt
        fields = [ 'pegawai_nama','pegawai_nip','jabatan','jenis_kegiatan','tempat_kegiatan', 'tgl_mulai_kegiatan', 'tgl_selesai_kegiatan',]

        widgets = {

            'pegawai_nama': forms.Textarea(attrs={'class': 'form-control'}),
            'pegawai_nip': forms.Textarea(attrs={'class': 'form-control'}),
            'jenis_kegiatan' : forms.TextInput({'class':'form-control'}),
            'tempat_kegiatan' : forms.TextInput({'class':'form-control'}),
            'tgl_mulai_kegiatan' : forms.DateInput({'class':'form-control','type': 'date'}),
            'tgl_selesai_kegiatan' : forms.DateInput({'class':'form-control','type': 'date'}),
        
        }
class SptUploadForm(forms.ModelForm):
    class Meta:
        model = Upload_Spt
        fields = ('nama', 'pdf_file')  # tambahkan kolom-kolom lain yang diperlukan

class JabatanForm(forms.ModelForm):
    class Meta:
        model = Jabatan
        fields = ['nama']