from django.db import models
from caching.base import CachingManager, CachingMixin
from localflavor.us.models import USStateField, PhoneNumberField
from datetime import datetime, date
from django.core.exceptions import ObjectDoesNotExist


"""
* Member Model: Contains only personal info, not year specific data
* Year-specific data is stored in a related model: Pass
* A Member can only have one pass for any pass season
* unless the pass has been flagged as Lost or Stolen.
"""
class Member(CachingMixin, models.Model):
    #objects = CachingManager()
    ### DORM CHOICES LIST ###
    # TODO: Complete the dorm choices
    DORM_CHOICES = (
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
    ### GENDER CHOICES LIST ###
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    
    ### TABLE ATTRIBUTES ###
    first_name = models.CharField(max_length=30,
                                  blank=False)
    
    last_name = models.CharField(max_length=50,
                                 blank=False)
    
    # not required    
    person_number = models.CharField(max_length=8,
                                     blank=True,
                                     help_text='The 8-digit number found on the bottom-right of a UB Student ID')
    
    local_address = models.CharField(max_length=50,
                                     blank=True)
    
    city = models.CharField(max_length=25,
                            default='Buffalo',
                            blank=False)
    
    state = USStateField(blank=False,
                         default='NY')
    
    zip_code = models.CharField(max_length=5,
                                blank=False,
                                default='14261')
    
    # not required
    dorm = models.CharField(max_length=4,
                            blank=True,
                            choices=DORM_CHOICES,
                            help_text='Choose from the list of dorms and leave zip code alone')
    
    email = models.EmailField(max_length=254,
                              blank=False,
                              verbose_name='E-mail Address')
    
    phone = PhoneNumberField(blank=False,
                                       help_text="Please use the format: XXX-XXX-XXXX")
    
    birthday = models.DateField(blank=False,
                                help_text="Please use the format: YYYY-MM-DD")
    
    gender = models.CharField(max_length=1,
                              blank=False,
                              default='M')
    # Photos
    # user photos are captured by the ID program and stored as binaries I think...
    # in general, this is bad practice and the photos shoud be saved as images in a directory.
    # however, I'm unsure about that fix at the moment
    # not required
    photo = models.BinaryField(blank=True,
                               null=True)
    
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    
    
    # joined class attributes
    
    # this displays as string on site
    def __unicode__(self):
        return self.first_name + " " + self.last_name
    
    def _dict(self):
        for i in self._meta.get_all_field_names():
            yield (i, getattr(self, i))
    
    def current_pass_list(self):
        from members.views import get_current_season # import this way to avoid cyclical imports
        #print get_current_season()
        #get current passes (deals with lost stolen)
        passes = self.pass_set.filter(season=get_current_season())
        #if no current passes get all passes
        if not passes:
          passes = self.pass_set.all()
          #if that worked, get just the most recent inactive pass
          if passes:
            #print passes
            passes = [passes[0]]
          #else they are a trip-only member and have no pass whatsoever
          else: 
            pseudo_pass = Pass(member_type='TRIP')
            #print 'Fake Pass', pseudo_pass
            passes = [pseudo_pass]
        return passes

    def pass_list(self):
        passes = self.current_pass_list()
        #if no current passes get all passes
        if not passes:
          passes = self.pass_set.all()
          #if that worked, get just the most recent inactive pass
          if passes:
            #print passes
            passes = [passes[0]]

        return passes
  
    def newest_pass(self):
        passes = self.pass_set.all()
        if passes:
            return passes[0]
        else:
            return False
    
"""
* The Pass model stores year-specific data about members
* Each member can have many passes, but only one active per season, where season is a pair of years
* e.g. (2014,2015) (ok, well the season fall and spring are actually full dataetimes, not years, but I digress)
* This allows for Lost/Stolen to be done easily
* This also allows us to track the evolution of a person throughout the club
"""
class Pass(CachingMixin, models.Model):
    #objects = CachingManager()
    ### PASS TYPE CHOICES LIST ###
    TYPE_CHOICES = (
        ('UB-Student', (
            ('FR' , 'Freshman'),
            ('SO' , 'Sophomore'),
            ('JR' , 'Junior'),
            ('SR', 'Senior'),
            ('SU', 'Super-Senior'),
          )
        ),
        ('Non-UB-Student', (
            # TODO: Fill this in with more local schools
            ('BS', 'Buffalo State'),
            ('ECC', 'Erie Community College'),
            ('CAN', 'Canisius College'),
            ('MED', 'Medaille College'),
            ('DAE', 'Daemon University'),
            ('NCCC', 'Niagara County Community College'),
          )
        ),
        ('Fac-Staff-Alum', (
            ('FAC', 'Faculty'),
            ('STA', 'Staff'),
            ('ALU', 'Alumni'),
          )
        ),
        ('FAM', 'Family'), # Family doesn't have a subtype
        ('VIP', 'Director/VIP'),
        ('TRIP', 'Trip-Only Member'),
    )
    
    ### TABLE ATTRIBUTES ###
    member = models.ForeignKey('Member')
    season = models.ForeignKey('Season')
    price_paid = models.PositiveIntegerField(default=0)
    # Photos
    # user photos are captured by the ID program and stored as binaries I think...
    # in general, this is bad practice and the photos shoud be saved as images in a directory.
    # however, I'm unsure about that fix at the moment
    # not required
    photo = models.BinaryField(blank=True,
                               null=True)
    is_reserved = models.BooleanField(default=False,
                                      help_text="Make Volunteers and Directors have low, reserved pass numbers",
                                      verbose_name="Reserved Number?",
                                      blank=False)
    active_id = models.PositiveIntegerField(blank=True,
                                            null=True,
                                            verbose_name='Pass Number for this season')
    member_type = models.ForeignKey('MemberType') 
    """
    member_type = models.CharField(max_length=4,
                                   blank=False,
                                   choices=TYPE_CHOICES,
                                   default='FR',
                                   db_column='type',
                                   help_text='Make sure to get the type correctly, as it determines the price',
                                   verbose_name='Member Pass Type')
    """
    lost_stolen = models.BooleanField(default=False)
    lost_stolen_note = models.TextField(blank=True)
    bus_flag = models.BooleanField(default=False)
    bus_flag_note = models.TextField(blank=True)
    pass_flag = models.BooleanField(default=False)
    pass_flag_note = models.TextField(blank=True)
    
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    
    def is_season_current(self):
        try:
            return self.season.is_current()
        except ObjectDoesNotExist:
            return False

    def __unicode__(self):
        return unicode(self.active_id)+": "+self.member.first_name + " " + self.member.last_name +", " + unicode(self.season)    
    
"""
* The Season model simply stores a pair of datetime.date(s) as 'Fall' and 'Spring' attributes
* Every Pass has a season associated with it
"""
class Season(models.Model):
    fall = models.DateField()
    spring = models.DateField()
    
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    
    def is_current(self):
        now = datetime.now()
        #TODO: Make this robust
        if (now.month <= 7):
            if ( now.year == self.spring.year ): return True
            else: return False
        else:
            if ( now.year == self.fall.year ): return True
            else: return False
    
    def __unicode__(self):
        return unicode(self.fall.year) + '-' + unicode(self.spring.year)
    
"""
* Member Type
"""
class MemberType(models.Model):
    parent_type = models.ForeignKey('MemberType', blank=True, null=True)
    member_type = models.CharField(max_length=50)
    type_abbr = models.CharField(max_length=4)

    def __unicode__(self):
        if self.parent_type:
            return self.parent_type.member_type +': '+ self.type_abbr + ' - '+self.member_type   
        else:
            return self.type_abbr + ' - ' + self.member_type

"""
* Price
* One interval of pricing associated a MemberType
"""
class Price(models.Model):
    member_type = models.ForeignKey('MemberType')
    start_date = models.DateField()
    end_date = models.DateField()
    price = models.PositiveIntegerField()

    def __unicode__(self):
        return unicode(self.member_type)+ ' - ' + unicode(self.price)
"""
    TYPE_CHOICES = (
        ('UB-Student', (
            ('FR' , 'Freshman'),
            ('SO' , 'Sophomore'),
            ('JR' , 'Junior'),
            ('SR', 'Senior'),
            ('SU', 'Super-Senior'),
          )
        ),
        ('Non-UB-Student', (
            # TODO: Fill this in with more local schools
            ('BS', 'Buffalo State'),
            ('ECC', 'Erie Community College'),
            ('CAN', 'Canisius College'),
            ('MED', 'Medaille College'),
            ('DAE', 'Daemon University'),
            ('NCCC', 'Niagara County Community College'),
          )
        ),
        ('Fac-Staff-Alum', (
            ('FAC', 'Faculty'),
            ('STA', 'Staff'),
            ('ALU', 'Alumni'),
          )
        ),
        ('FAM', 'Family'), # Family doesn't have a subtype
        ('VIP', 'Director/VIP'),
        ('TRIP', 'Trip-Only Member'),
    )
"""
