from django.forms import ModelForm
from adkep.models import Pegawai, Absen
from django import forms

class FromPegawai(ModelForm):
    class Meta:
        model = Pegawai
        fields = '__all__'

        widgets = {
            'nama' : forms.TextInput({'class':'form-control'}),
            'nrp' : forms.TextInput({'class':'form-control'}),
            'email' : forms.TextInput({'class':'form-control'}),
            'hp' : forms.TextInput({'class':'form-control'}),
            'alamat' : forms.TextInput({'class':'form-control'}),
            'jabatan' : forms.TextInput({'class':'form-control'}),
            'absen_id' : forms.Select({'class':'form-control'})
        }

class FromAbsen(ModelForm):
    class Meta:
        model = Absen
        fields = '__all__'

        widgets = {
           
            'status' : forms.TextInput({'class':'form-control'}),
            'keterangan' : forms.TextInput({'class':'form-control'}),
        }