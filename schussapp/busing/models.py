from django.db import models

from datetime import datetime, date

from members.models import Member


"""
 * Bus model:
 * Has list of members, capacity, date, destination, number, 
"""
class Bus(models.Model):
    capacity = models.PositiveIntegerField()
    date = models.DateField()
    number = models.PositiveIntegerField()
    
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    #event # optional
    
    def __unicode__(self):
        return unicode(self.number) + " " + unicode(self.date)
    
"""
 * Bus Checkin
 * Has a member, and pick-up location
"""
class BusCheckin(models.Model):
    # Pick-up locations
    STOPS = (('GOV', 'Governors'),
             ('ELLI', 'Ellicot'),
             ('MAIN', 'Main St'),    
        ) 
    
    member = models.ForeignKey(Member)
    bus = models.ForeignKey(Bus)
    pickup = models.CharField(max_length=5, choices=STOPS)
    
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    
    def __unicode__(self):
        return unicode(self.member)