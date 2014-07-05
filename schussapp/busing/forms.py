from django import forms

from busing.models import Bus

class BusForm(forms.ModelForm):
    class Meta:
        model = Bus
        fields = ('number', 'capacity', 'date')
        widgets = {
            'number': forms.NumberInput(attrs={'class':'form-control', 'placeholder':42}),
            'capacity': forms.NumberInput(attrs={'class':'form-control', 'placeholder':52}),
            'date': forms.DateInput(attrs={'class':'form-control'})
        }
