# django imports
from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from django.contrib import messages
from django.http import Http404

from busing.models import Bus
from busing.forms import BusForm

from members.models import Member, Pass, Season
from members.views import get_current_season

from datetime import date, datetime

# Create your views here.
"""
 * Bus Home Page
 * Display buses for today if no date given in in url
"""
def busing_home(request, date=datetime.strftime(date.today(), '%Y-%m-%d')):
    context= {'active':'busing'}
    active_members = Member.objects.filter(pass__season=get_current_season())
    context['active_members'] = active_members
    print active_members
    #context['bus_options'] = Bus.objects.all()
    date = datetime.strptime(date, '%Y-%m-%d').date()  # format input date as date object
    context['date'] = date
    context['today_list'] = Bus.objects.filter(date = date)
    context['bus_list'] = Bus.objects.all()
    print context['bus_list']
    
    return render(request, "busing/busing_home.html", context)

"""
 * Add Bus to the system
"""
def busing_add(request):
    context= {'active':'busing'}
    if request.method == 'POST':
        bus_form = BusForm(request.POST)
        if bus_form.is_valid():
            bus = Bus(**bus_form.cleaned_data)
            bus.save()
            print bus
            return redirect('busing_home', date=datetime.strftime(bus.date, '%Y-%m-%d'))
        else:
            context['add_bus_form'] = bus_form
    else:
        context['add_bus_form'] = BusForm()
    
    return render(request, "busing/busing_add.html", context)