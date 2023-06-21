from django import forms
from django.forms import ModelForm
from decimal import Decimal
from .models import Absen
from adkep.models import JabatanStruktural

class JabatanStrukturalForm(ModelForm):
    class Meta:
        model = JabatanStruktural
        fields = '__all__'

class AbsenForm(forms.ModelForm):
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
    PRODI_CHOICES = [
        ('teknik elektronika industri', 'Teknik Elekronika Industri'),
        ('akutansi', 'Akutansi'),
        ('teknik informasi', 'Teknologi Informasi'),
        ('mekatronika', 'Mekatronika'),
        ('-', '-')
    ]
    
    jabatanstruktural = forms.ModelChoiceField(queryset=JabatanStruktural.objects.all(), empty_label=None, widget=forms.Select(attrs={'class': 'form-control'}))
    unit = forms.ChoiceField(choices=UNIT_CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))
    program_studi = forms.ChoiceField(choices=PRODI_CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))
    
    class Meta:
        model = Absen
        fields = '__all__'
        widgets = {
            'nama': forms.TextInput(attrs={'class': 'form-control'}),
            'nip': forms.TextInput(attrs={'class': 'form-control'}),
            'tempat_tgl_lahir': forms.TextInput(attrs={'class': 'form-control'}),
            'pangkat_gol_ruang_tmt': forms.TextInput(attrs={'class': 'form-control'}),
            'tanggal': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'alasan': forms.Textarea(attrs={'class': 'form-control'}),
            'masuk': forms.TimeInput(attrs={'class': 'form-control', 'type': 'time'}),
            'pulang': forms.TimeInput(attrs={'class': 'form-control', 'type': 'time'}),
            'jumlah_jam': forms.NumberInput(attrs={'class': 'form-control', 'readonly': 'readonly'}),
            'jumlah_potongan_tukin': forms.NumberInput(attrs={'class': 'form-control', 'readonly': 'readonly'}),
        }

    