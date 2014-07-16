from django.db import models

from datetime import datetime, date

from members.models import Pass

"""
 * Unique bus number for the waiting list (which is really just another bus)
"""
WAIT_LIST_NUM = 888888
WAIT_LIST_CAP = 100

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

    # get list of all reservations for this bus
    def res_list(self):
        res_list = BusCheckin.objects.filter(bus=self)
        #print res_list
        return res_list

    def n_open_seats(self):
        #print int(self.capacity)
        #print len(self.res_list())
        return int(self.capacity) - len(self.res_list())

    def is_open(self):
        return self.n_open_seats() > 0

    def __unicode__(self):
        return unicode(self.number) + " " + unicode(self.date)

    
"""
 * Bus Checkin
 * Has a member, and pick-up location
"""
# Pick-up locations
STOPS = (('GOV', 'Governors'),
     ('ELLI', 'Ellicot'),
     ('MAIN', 'Main St'),    
) 
class BusCheckin(models.Model):
    
    member = models.ForeignKey(Pass)
    bus = models.ForeignKey(Bus)
    pickup = models.CharField(max_length=5, choices=STOPS)
    
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    
    def __unicode__(self):
        return unicode(self.member.active_id) +': '+unicode(self.member.member)+ ' - '+ unicode(self.bus.number)
