from django import forms

from busing.models import Bus, STOPS

class BusForm(forms.ModelForm):
    class Meta:
        model = Bus
        fields = ('number', 'capacity', 'date')
        widgets = {
            'number': forms.NumberInput(attrs={'class':'form-control', 'placeholder':42}),
            'capacity': forms.NumberInput(attrs={'class':'form-control', 'placeholder':52}),
            'date': forms.DateInput(attrs={'class':'form-control'})
        }

class BusCheckinForm(forms.Form):
    pass_num = forms.IntegerField(min_value=1, max_value=999,
                             widget=forms.NumberInput(attrs={ 'class':'form-control pass_search','placeholder':'42'}))
    first_name = forms.CharField(max_length=30,
                             widget=forms.TextInput(attrs={ 'class':'form-control first_search',
                                                            'placeholder':'First'}))

    last_name = forms.CharField(max_length=50,
                             widget=forms.TextInput(attrs={ 'class':'form-control last_search',
                                                            'placeholder':'Last'}))

    pickup = forms.ChoiceField(choices=STOPS, widget=forms.RadioSelect())
    bus = forms.ModelChoiceField(queryset=Bus.objects.all())
    
    
