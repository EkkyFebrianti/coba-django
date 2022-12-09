from django import forms
from django.forms import ModelForm
from dashboard.models import Barang


class FormBarang(ModelForm):
    class Meta:
        model = Barang
        fields = '__all__'

        widgets = {
            # nama pada widget harus sana dengan pada file models.py
            'kodebrg': forms.TextInput({'class': 'form-control'}),
            'nama': forms.TextInput({'class': 'form-control'}),
            'stok': forms.NumberInput({'class': 'form-control'}),
            'harga': forms.NumberInput({'class': 'form-control'}),
            'link_gbr': forms.Select({'class': 'form-control'}),
        }
