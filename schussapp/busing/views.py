# django imports
from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from django.contrib import messages
from django.http import Http404
from django.db.models import Q
from django.core.exceptions import ObjectDoesNotExist

from busing.models import Bus, BusCheckin, WAIT_LIST_NUM, WAIT_LIST_CAP
from busing.forms import BusForm, BusCheckinForm

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
    actives = Pass.objects.filter(season=get_current_season()).order_by('active_id')
    context['actives'] = actives
    inactives = Member.objects.filter(~Q(pass__season=get_current_season())).order_by('last_name')
    context['inactives'] = inactives
    date = datetime.strptime(date, '%Y-%m-%d').date()  # format input date as date object
    context['date'] = date
    context['today_list'] = Bus.objects.filter( ~Q(number=WAIT_LIST_NUM), date=date) #exclude wait list
    context['bus_list'] = Bus.objects.filter(~Q(number=WAIT_LIST_NUM))
    context['days_list'] = { bus.date for bus in context['bus_list'] } # set of unique dates
    print context['days_list'] 
    #get waiting list bus or create it
    try:
      wait = Bus.objects.get(number=WAIT_LIST_NUM, date=date)
    except ObjectDoesNotExist:
      wait = Bus(number=WAIT_LIST_NUM, capacity=WAIT_LIST_CAP, date=date)
      wait.save()
    context['waiting_list'] = wait
    #print 'Wat:',wait 
   
    # check to see if a bus reservation has been posted
    if request.method == 'POST':
        form = BusCheckinForm(request.POST)
        if form.is_valid():
            #print form.cleaned_data
            member_pass = get_object_or_404(Pass, active_id=form.cleaned_data['pass_num'], season=get_current_season())
            bus = form.cleaned_data['bus']
            # don't want to overcrowd buses
               
            if bus.is_open():
              # if they are on the waiting list, switch them to this bus
              wait_list = [bc.member for bc in wait.res_list()]
              if member_pass in wait_list:
                checkin = BusCheckin.objects.get(bus=wait, member=member_pass)
                checkin.pickup=form.cleaned_data['pickup']
                checkin.save()
                return redirect('buscheckin_switch', res_id=checkin.id, bus_id=bus.id)

              # check to see if they are on any bus already
              res_list = []
              for other_bus in context['today_list']:
                m_list = [ bc.member for bc in other_bus.res_list()]
                for mem in m_list:res_list.append(mem)   
              print 'list:', res_list
              if member_pass not in res_list:
                pickup = form.cleaned_data['pickup']
                checkin = BusCheckin(member=member_pass, bus=bus, pickup=pickup)
                #print 'Checkin:', checkin
                checkin.save()
            
            
    else:
        context['checkin_form'] = BusCheckinForm()
 
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
     #       print bus
            return redirect('busing_home', date=datetime.strftime(bus.date, '%Y-%m-%d'))
        else:
            context['add_bus_form'] = bus_form
    else:
        context['add_bus_form'] = BusForm()
    
    return render(request, "busing/busing_add.html", context)

"""
 * Edit Existing Bus
"""
def busing_edit(request, id=None):
    context = {'active':'busing'}
    bus = get_object_or_404(Bus, pk=id)
    context['bus'] = bus
    if request.method == 'POST' :
       form = BusForm(request.POST)
       if form.is_valid():
          bus.number=form.cleaned_data['number']
          bus.capacity=form.cleaned_data['capacity']
          bus.date=form.cleaned_data['date']
          bus.save()
          return redirect('busing_home', date=datetime.strftime(bus.date,'%Y-%m-%d'))
       else:
          context['edit_bus_form'] = form
    else:
#      form = BusForm( number=bus.number, capacity=bus.capacity, date=bus.date)
      form = BusForm(instance=bus)
      #print form
      context['edit_bus_form'] = form
    
    return render(request, 'busing/busing_edit.html', context)
        
"""
* Remove an Existing Bus
* NOTE: This alters the database
"""
def busing_remove(request, id=None):
  context = {'active':'busing'}
  bus = get_object_or_404(Bus, pk=id)
  # if there were any other buses on that day, lets go back there
  others_from_day = Bus.objects.filter(date=bus.date)
  if others_from_day:
    date=datetime.strftime(bus.date,'%Y-%m-%d')
  else:
    date=''
  bus.delete()
  return redirect('busing_home', date=date)
    
"""
* Remove an Existing BusCheckin
* NOTE: This alters the database
"""
def buscheckin_remove(request, id=None):
  context = {'active':'busing'}
  checkin = get_object_or_404(BusCheckin, pk=id)
  date = datetime.strftime(checkin.bus.date, '%Y-%m-%d')
  checkin.delete()
  return redirect('busing_home', date=date)

def buscheckin_switch(request, res_id=None, bus_id=None):
  context = {'active':'busing'}
  checkin = get_object_or_404(BusCheckin, pk=int(res_id))
  date = datetime.strftime(checkin.bus.date, '%Y-%m-%d')
  bus = get_object_or_404(Bus, pk=int(bus_id))
  if bus.is_open(): 
    checkin.bus = bus
    checkin.save()
  return redirect('busing_home', date=date)












