from django import forms

from trips.models import Trip, TripEnrollment

class TripForm(forms.ModelForm):
    class Meta:
        model = Trip
        fields = ( 'name', 'capacity', 'start_date', 'end_date',
                    'down_payment_due', 'final_payment_due', 
                    'member_price', 'nonmember_price', 'other_price',
                    'destination_address', 'city', 'state', 'zip_code')
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Gnar Mountain'}),
            'capacity': forms.NumberInput(attrs={'class':'form-control', 'placeholder':52}),
            'start_date': forms.DateInput(attrs={'class':'form-control', 'placeholder':'Leave'}),
            'end_date': forms.DateInput(attrs={'class':'form-control', 'placeholder':'Return'}),
            'down_payment_due': forms.DateInput(attrs={'class':'form-control', 'placeholder':'Down Payment Due Date'}),
            'final_payment_due': forms.DateInput(attrs={'class':'form-control', 'placeholder':'Final Payment Due Date'}),
            'member_price':forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Members'}),
            'nonmember_price':forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Non-Members'}),
            'other_price':forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Other'}),
            'destination_address':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Street'}),
            'city':forms.TextInput(attrs={'class':'form-control', 'placeholder':'City'}),
            'state':forms.TextInput(attrs={'class':'form-control', 'placeholder':'State'}),
            'zip_code':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Zip'})
        }

class TripEnrollmentForm(forms.ModelForm):
    class Meta:
        model = TripEnrollment
        fields = ( 'price_paid',)
        widgets = {
            'price_paid': forms.NumberInput(attrs={'class':'form-control'})
        }
    
    
