from django.forms import ModelForm
from perizinan.models import Cutiizin, Spt
from django import forms

class FromCuti(ModelForm):
    class Meta:
        model = Cutiizin
        fields = '__all__'

        widgets = {
            'nama' : forms.TextInput({'class':'form-control'}),
            'nrp' : forms.TextInput({'class':'form-control'}),
            'jabatan' : forms.TextInput({'class':'form-control'}),
            'keperluan' : forms.TextInput({'class':'form-control'}),
            'tgl_mulai' : forms.DateInput({'class':'form-control'}),
            'tgl_selesai' : forms.DateInput({'class':'form-control'}),
            
        }

class FromSpt(ModelForm):
    class Meta:
        model = Spt
        fields = '__all__'

        widgets = {

            'nama' : forms.TextInput({'class':'form-control'}),
            'nrp' : forms.TextInput({'class':'form-control'}),
            'jenis_kegiatan' : forms.TextInput({'class':'form-control'}),
            'tempat_kegiatan' : forms.TextInput({'class':'form-control'}),
            'tgl_mulai_kegiatan' : forms.DateInput({'class':'form-control'}),
            'tgl_selesai_kegiatan' : forms.DateInput({'class':'form-control'}),
        
        }