from django import forms
from localflavor.us.forms import USStateField, USPhoneNumberField #, USZipCodeField
from members.models import Pass, Season, MemberType, Price


class NewMemberForm(forms.Form):
    ### DORM CHOICES LIST ###
    # TODO: Complete the dorm choices
    DORM_CHOICES = (
        (None, 'None'),
        ('Ellicot', (
            ('SPA', 'Spaulding'),
            ('POR', 'Porter'),
            ('WIL', 'Wilkeson'),
            ('RICH', 'Richmond'),
            ('RED', 'Red Jacket'),
          )
        ),
        ('Governors', (
            ('ROS', 'Rosevelt'),
            ('DEW', 'Dewey'),
            ('CLI', 'Clement'),
            ('LEH', 'Lehman'),
          )   
        ),
        ('Main St.', (
            ('CLE', 'Clemens'),
            ('GOOD', 'Goodyear'),
          )
        ),
        ('GRE', 'Greiner'),
    )
    ### PASS TYPE CHOICES LIST ###
    ### GENDER CHOICES LIST ###
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    ### DYNAMIC LIST OF POSSIBLE RESERVED IDS FOR CURRENT SEASON ###
    current_season = Season.objects.latest('spring')
    active_reserved = Pass.objects.filter(season=current_season, active_id__gte=2, active_id__lte=25)
    taken_actives_set = [ int(p.active_id) for p in active_reserved]
    UNRESERVED_ACTIVES = [(r,r) for r in range(2,26) if r not in taken_actives_set]

    
    ### MEMBER ATTRIBUTES ###
    first_name = forms.CharField(max_length=30,
                                 widget=forms.TextInput(attrs={'class':'form-control',
                                                               'placeholder':'First Name'})) 
    last_name = forms.CharField(max_length=50,
                                widget=forms.TextInput(attrs={'class':'form-control',
                                                               'placeholder':'Last Name'}))
    
    # not required    
    person_number = forms.CharField(max_length=8, required=False,
                                widget=forms.TextInput(attrs={'class':'form-control',
                                                               'placeholder':'Person Number'}))
    
    local_address = forms.CharField(max_length=50, required=False,
                                widget=forms.TextInput(attrs={'class':'form-control',
                                                               'placeholder':'Street'}))
    
    city = forms.CharField(max_length=25, initial='Buffalo',
                                widget=forms.TextInput(attrs={'class':'form-control'}))
    
    state = USStateField(initial='NY',
                                widget=forms.TextInput(attrs={'class':'form-control'}))
    
    zip_code = forms.CharField(max_length=5, initial='14261',
                                widget=forms.TextInput(attrs={'class':'form-control'}))

    
    # not required
    dorm = forms.ChoiceField(required=False, choices=DORM_CHOICES,
                             widget=forms.Select(attrs={'class':'form-control'}))
    
    email = forms.EmailField(max_length=254,
                                widget=forms.TextInput(attrs={'class':'form-control',
                                                               'placeholder':'schuss.is.awesome@fursure.com'}))
    
    phone = USPhoneNumberField(
                                widget=forms.TextInput(attrs={'class':'form-control',
                                                               'placeholder':'716-645-3100'}))
    
    birthday = forms.DateField(
                                widget=forms.TextInput(attrs={'class':'form-control',
                                                               'placeholder':'1/1/1960'}))
    
    gender = forms.ChoiceField(choices=GENDER_CHOICES,
                               widget=forms.Select(attrs={'class':'form-control'}))
    
    ### PASS ATTRIBUTES ###
    member_type = forms.ModelChoiceField(queryset=MemberType.objects.exclude(type_abbr="STU").exclude(type_abbr="NSTU"),
                             empty_label=None,
                             widget=forms.Select(attrs={'class':'form-control'}))
    is_reserved = forms.BooleanField(required=False, help_text='Give volunteers and office staff low numbers',
                                widget=forms.CheckboxInput(attrs={'class':'checkbox'})
                                     )
    reserved_id = forms.ChoiceField(choices=UNRESERVED_ACTIVES, required=False,
                                    help_text='Only works if "Is Reserved" is checked',
                                    widget=forms.Select(attrs={'class':'form-control', 'disabled':''}))
    
class EditMemberForm(forms.Form):
    ### DORM CHOICES LIST ###
    # TODO: Complete the dorm choices
    DORM_CHOICES = (
        (None, 'None'),
        ('Ellicot', (
            ('SPA', 'Spaulding'),
            ('POR', 'Porter'),
            ('WIL', 'Wilkeson'),
            ('RICH', 'Richmond'),
            ('RED', 'Red Jacket'),
          )
        ),
        ('Governors', (
            ('ROS', 'Rosevelt'),
          )   
        ),
        ('Main St.', (
            ('CLE', 'Clemens'),
            ('GOOD', 'Goodyear'),
          )
        ),
        ('GRE', 'Greiner'),
    )
    ### PASS TYPE CHOICES LIST ###
    ### GENDER CHOICES LIST ###
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    ### DYNAMIC LIST OF POSSIBLE RESERVED IDS FOR CURRENT SEASON ###
    current_season = Season.objects.latest('spring')
    active_reserved = Pass.objects.filter(season=current_season, active_id__gte=2, active_id__lte=25)
    taken_actives_set = [ int(p.active_id) for p in active_reserved]
    UNRESERVED_ACTIVES = [(r,r) for r in range(2,26) if r not in taken_actives_set]
    
    ### MEMBER ATTRIBUTES ###
    first_name = forms.CharField(max_length=30,
                                 widget=forms.TextInput(attrs={'class':'form-control',
                                                               'placeholder':'First Name'})) 
    last_name = forms.CharField(max_length=50,
                                widget=forms.TextInput(attrs={'class':'form-control',
                                                               'placeholder':'Last Name'}))
    
    # not required    
    person_number = forms.CharField(max_length=8, required=False,
                                widget=forms.TextInput(attrs={'class':'form-control',
                                                               'placeholder':'Person Number'}))
    
    local_address = forms.CharField(max_length=50, required=False,
                                widget=forms.TextInput(attrs={'class':'form-control',
                                                               'placeholder':'Street'}))
    
    city = forms.CharField(max_length=25, initial='Buffalo',
                                widget=forms.TextInput(attrs={'class':'form-control'}))
    
    state = USStateField(initial='NY',
                                widget=forms.TextInput(attrs={'class':'form-control'}))
    
    zip_code = forms.CharField(max_length=5, initial='14261',
                                widget=forms.TextInput(attrs={'class':'form-control'}))

    
    # not required
    dorm = forms.ChoiceField(required=False, choices=DORM_CHOICES,
                             widget=forms.Select(attrs={'class':'form-control'}))
    
    email = forms.EmailField(max_length=254,
                                widget=forms.TextInput(attrs={'class':'form-control',
                                                               'placeholder':'schuss.is.awesome@fursure.com'}))
    
    phone = USPhoneNumberField(
                                widget=forms.TextInput(attrs={'class':'form-control',
                                                               'placeholder':'716-645-3100'}))
    
    birthday = forms.DateField(
                                widget=forms.TextInput(attrs={'class':'form-control',
                                                               'placeholder':'1/1/1960'}))
    
    gender = forms.ChoiceField(choices=GENDER_CHOICES,
                               widget=forms.Select(attrs={'class':'form-control'}))
    
    ### PASS ATTRIBUTES ###
    member_type = forms.ModelChoiceField(queryset=MemberType.objects.exclude(type_abbr="STU").exclude(type_abbr="NSTU"),
                             empty_label=None,
                             widget=forms.Select(attrs={'class':'form-control'}))
    member_id = forms.IntegerField(required=True,
                                widget=forms.NumberInput(attrs={'class':'form-control'}))
    active_id = forms.IntegerField(required=False,
                                widget=forms.NumberInput(attrs={'class':'form-control'}))
    is_reserved = forms.BooleanField(required=False, help_text='Give volunteers and office staff low numbers',
                                widget=forms.CheckboxInput(attrs={'class':'checkbox'})
                                     )
    reserved_id = forms.ChoiceField(choices=UNRESERVED_ACTIVES, required=False,
                                    help_text='Only works if "Is Reserved" is checked',
                                    widget=forms.Select(attrs={'class':'form-control', 'disabled':''}))
    
class LostStolenForm(forms.Form):                    
    lost_stolen_note = forms.CharField(required=False,
                                       widget=forms.Textarea(attrs={'class':'form-control',
                                                                    'placeholder':'Please enter a short description'}))
                                       
class BusFlagForm(forms.Form):                           
    bus_flag_note = forms.CharField(required=False,
                                    widget=forms.Textarea(attrs={'class':'form-control',
                                                                 'placeholder':'Please enter a short description'}))
    
class PassFlagForm(forms.Form):
    pass_flag_note = forms.CharField(required=False,
                                     widget=forms.Textarea(attrs={'class':'form-control',
                                                                  'placeholder':'Please enter a short description'}))

    
