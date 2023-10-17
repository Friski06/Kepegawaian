from django import forms
from django.forms import ModelForm
from decimal import Decimal
from .models import Absen
from adkep.models import JabatanBawahan


class AbsenForm(forms.ModelForm):
   
    
    jabatan = forms.ModelChoiceField(queryset=JabatanBawahan.objects.all(), empty_label=None, widget=forms.Select(attrs={'class': 'form-control'}))
    
    
    class Meta:
        model = Absen
        fields = '__all__'
        exclude = ['user','status','pegawaipribadi','pegawaipekerjaan','jumlah_jam','jumlah_potongan_tukin']
        widgets = {
            
            
            'tanggal': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'alasan': forms.Textarea(attrs={'class': 'form-control'}),
            'masuk': forms.TimeInput(attrs={'class': 'form-control', 'type': 'time'}),
            'pulang': forms.TimeInput(attrs={'class': 'form-control', 'type': 'time'}),
            'jumlah_jam': forms.NumberInput(attrs={'class': 'form-control', 'readonly': 'readonly'}),
            'jumlah_potongan_tukin': forms.NumberInput(attrs={'class': 'form-control', 'readonly': 'readonly'}),
        }

    