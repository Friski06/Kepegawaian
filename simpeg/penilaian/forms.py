from django.forms import ModelForm
from django import forms
from penilaian.models import Nilai




class FromNilai(ModelForm):
    
    class Meta:
        model = Nilai
        fields = ('kerapian','kesopanan','dedikasi', 'loyalitas', 'disiplin','kerjasama','tupoksi',)

        widgets = {     
            'kerapian' : forms.TextInput({'class':'form-control'}),
            'kesopanan' : forms.TextInput({'class':'form-control'}),
            'dedikasi' : forms.TextInput({'class':'form-control'}),
            'loyalitas' : forms.TextInput({'class':'form-control'}),
            'disiplin' : forms.TextInput({'class':'form-control'}),
            'kerjasama ' : forms.TextInput({'class':'form-control'}),
            'tupoksi' : forms.TextInput({'class':'form-control'}),
            
        }