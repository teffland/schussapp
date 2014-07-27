from django.db import models
from localflavor.us.models import USStateField, PhoneNumberField

from datetime import datetime, date

from members.models import Pass, Season


"""
 * Trip model:
 * Fields:
 *      capacity, name, Season, destination (address),
 *      start_date, end_date, down_payment_due, final_payment_due,
 *      member_price, nonmember_price,
 *      created, modified
 * Methods:
 *  reslist - returns list of TripEnrollments for this trip
 *  n_open_seats - returns number of open seats
 *  is_open - returns whether n_open_seats() > 0
"""
class Trip(models.Model):
    name = models.CharField(max_length=50)
    capacity = models.PositiveIntegerField()
    start_date = models.DateField()
    end_date = models.DateField()

    down_payment_due = models.DateField(null=True)
    final_payment_due = models.DateField(null=True)
    
    season = models.ForeignKey(Season)
    
    member_price = models.PositiveIntegerField()
    nonmember_price = models.PositiveIntegerField()
    other_price = models.PositiveIntegerField(null=True, blank=True)

    
    # Destination Address Stuff
    destination_address = models.CharField(max_length=50)
    city = models.CharField(max_length=25)
    state = USStateField(blank=True, null=True) # can be null if trip goes out of US
    zip_code = models.CharField(max_length=5, blank=True, null=True) # see above
     
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    # get list of all reservations for this bus
    def res_list(self):
        res_list = TripEnrollment.objects.filter(trip=self)
        #print res_list
        return res_list

    def n_open_seats(self):
        #print int(self.capacity)
        #print len(self.res_list())
        return int(self.capacity) - len(self.res_list())

    def is_open(self):
        return self.n_open_seats() > 0

    def __unicode__(self):
        return unicode(self.name) + " (" + unicode(self.start_date) +' - '+ unicode(self.end_date)+')'

    
"""
 * Trip Enrollment:
 * Fields:
 *      member_pass, trip, price paid, created, modified
"""
class TripEnrollment(models.Model):
    
    member_pass = models.ForeignKey(Pass)
    trip = models.ForeignKey(Trip)
    price_paid = models.PositiveIntegerField()
    
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    
    def __unicode__(self):
        return unicode(self.member_pass) +': '+unicode(self.trip)
