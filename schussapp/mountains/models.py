from django.db import models
from localflavor.us.models import USStateField, PhoneNumberField

from datetime import datetime, time

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
        if slots:
            any_open = [slot.is_open() for slot in slots]
            return sum(any_open) # if any are true, they will sum to true

        else:
            return True

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
    mountain = models.ForeignKey("Mountain")
    season = models.ForeignKey(Season)

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def is_open(self):
        now = time.now()
        print now
        return now >= self.start_time and now <= self.end_time

    def __unicode__(self):
        return unicode(self.mountain) + ": " + unicode(self.start_time)+' - '+ unicode(self.end_time)


