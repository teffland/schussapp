from django.test import TestCase

from members.models import Member, Pass, Season

import datetime
# Create your tests here.

class SeasonTestCase(TestCase):
    # if there is no season installed at all,
    # create one for the year this was made
    # (should only matter for testing)
    def setUp(self):
        if not Season.objects.all():
            season = Season(fall='2013-08-01', spring='2014-07-31')
            

