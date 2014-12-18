from django.db import models
from localflavor.us.models import USStateField, PhoneNumberField

from datetime import datetime, time, date

from members.models import Pass, Season

"""
 * Mountain:
 * Fields:
 *  name, address, city, state, zip
"""
class Mountain(models.Model):

    # the important stuff
    name = models.CharField(max_length=50)
    abbr = models.CharField(max_length=5)
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=25)
    state = USStateField(blank=False, default='NY')
    zip_code = models.CharField(max_length=5)
    
    phone = PhoneNumberField()

    # optional useless factoids
    vertical = models.PositiveIntegerField(null=True, blank=True)
    num_lifts = models.PositiveIntegerField(null=True, blank=True)
    num_trails = models.PositiveIntegerField(null=True, blank=True)
    ski_acre = models.PositiveIntegerField(null=True, blank=True)

    # bookkeeping timestamps
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def is_open(self):
        slots = MountainScheduleSlot.objects.filter(mountain=self)
        print 'slots:', slots
        if slots:
            """
            print "Are they open?"
            for slot in slots:
                #print slot
                print slot.is_free()
            any_open = [slot.is_free() for slot in slots]
            print any_open
            return sum(any_open) # if any are true, they will sum to true
            """   
            return True
        else:
            return True

    def todays_checkins(self):
        checkins = MountainCheckin.objects.filter(mountain=self)
        todays = [checkin for checkin in checkins if checkin.is_on_day(date.today())]
        return todays
    
    def __unicode__(self):
        return self.name

"""
 * Mountain Checkin:
 *   A specific instance of a member with a pass checking in to ride at a Mountain
 * Fields:
 *   member_pass, mountain, checkin_time (created)
 * Methods:
 *
"""
class MountainCheckin(models.Model):

    member_pass = models.ForeignKey(Pass)
    mountain = models.ForeignKey('Mountain')

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def is_on_day(self, date):
        print self.created.date()
        return self.created.date() == date

    def __unicode__(self):
        return unicode(self.member_pass.member) + ' at ' + unicode(self.mountain) +' : ' + unicode(self.created)

"""
 * MountainScheduleSlot
 *   An interval of time when passes are allowed to check in at that mountain
 * Fields:
 *   start_time, end_time, Mountain, Season
 * Methods:
 *
"""
class MountainScheduleSlot(models.Model):

    start_time = models.TimeField()
    end_time = models.TimeField()
    sunday = models.BooleanField(default=False)
    monday = models.BooleanField(default=False)
    tuesday = models.BooleanField(default=False)
    wednesday = models.BooleanField(default=False)
    thursday = models.BooleanField(default=False)
    friday = models.BooleanField(default=False)
    saturday = models.BooleanField(default=False)

    mountain = models.ForeignKey("Mountain")
    season = models.ForeignKey(Season)

    price = models.PositiveSmallIntegerField(default=0)

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def is_free(self):
        today = date.weekday()
        print "Today is ", today
        if today == 0 and self.sunday == False: return False 
        elif today == 1 and self.monday == False: return False 
        elif today == 2 and self.tuesday == False: return False 
        elif today == 3 and self.wednesday == False: return False 
        elif today == 4 and self.thursday == False: return False 
        elif today == 5 and self.friday == False: return False 
        elif today == 6 and self.saturday == False: return False 
        else: # so we're open today, but is the time slot correct?
            now = datetime.now().time()
            #print now
            if now >= self.start_time and now <= self.end_time: return True
            else: return False

    def __unicode__(self):
        return unicode(self.mountain) + ": " + unicode(self.start_time)+' - '+ unicode(self.end_time)


