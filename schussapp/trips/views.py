# django imports
from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from django.contrib import messages
from django.http import Http404
from django.db.models import Q


from trips.models import Trip, TripEnrollment
from trips.forms import TripForm, TripEnrollmentForm

from members.models import Member, Pass, Season
from members.views import get_current_season

"""
 * Trip Home
 * Shows list of trips
"""
def trips_home(request):
  context = {'active':'trips'}
  context['trips'] = Trip.objects.all()

  return render(request, 'trips/trips_home.html', context)

"""
 * View a specific trip
"""
def trips_view(request, trip_id=None):
  context = {'active':'trips'}
  trip = get_object_or_404(Trip, pk=int(trip_id))
  context['trip'] = trip

  #get current members
  context['filter_list'] = Member.objects.filter( ~Q(pass__tripenrollment__trip=trip), pass__season=get_current_season())

  return render(request, 'trips/trips_view.html', context)

"""
 * Create a new trip
"""
def trips_add(request):
  context = {'active':'trips'}
  if request.method == 'POST':
    trip_form = TripForm(request.POST)
    if trip_form.is_valid():
      season = get_current_season()
      trip = Trip(season=season, **trip_form.cleaned_data)
      trip.save()
      return redirect('trips_view', trip_id = trip.id)
    else:
        context['add_trip_form'] = trip_form
  else:
    context['add_trip_form'] = TripForm()

  return render(request, 'trips/trips_add.html', context)

"""
 * Edit a trip
"""
def trips_edit(request, trip_id=None):
  context = {'active':'trips'}

  trip = get_object_or_404(Trip, pk=int(trip_id))
  context['trip'] = trip
  if request.method == 'POST':
    trip_form = TripForm(request.POST)
    if trip_form.is_valid():
      for k,v in trip_form.cleaned_data.items():
        trip.__dict__[k] = v
      trip.save()
      return redirect('trips_view', trip_id = trip.id)
    else:
        context['edit_trip_form'] = trip_form
  else:
    context['edit_trip_form'] = TripForm(instance=trip)

  return render(request, 'trips/trips_edit.html', context)

"""
 * 
"""
def trips_remove(request, trip_id=None):
  context = {'active':'trips'}

  return render(request, 'trips/trips_home.html', context)

"""
 * Add a member to a trip
"""
def enrollment_add(request, pass_id=None, trip_id=None):
  context = {'active':'trips'}

  # get the pass and trip we want to enroll
  member_pass = get_object_or_404(Pass, pk=int(pass_id))
  context['pass'] = member_pass
  trip = get_object_or_404(Trip, pk=int(trip_id))
  context['trip'] = trip

  if request.method == 'POST':
    trip_enroll_form = TripEnrollmentForm(request.POST)
    if trip_enroll_form.is_valid():
      trip_enroll = TripEnrollment(member_pass=member_pass, trip=trip, 
                                   price_paid=trip_enroll_form.cleaned_data['price_paid'])
      trip_enroll.save()
      return redirect('trips_view', trip_id=trip.id)

    else:
      context['trip_enroll_form'] = trip_enroll_form
  else:
    trip_enroll = TripEnrollment.objects.get(member_pass=member_pass, trip=trip)
    if trip_enroll:
      return redirect('trips_view', trip_id=trip.id)
    else:
      context['trip_enroll_form'] = TripEnrollmentForm()

  return render(request, 'trips/trips_enroll.html', context)

"""
 * Edit a trip enrollment 
"""
def enrollment_edit(request, enroll_id=None):
  context = {'active':'trips'}
  trip_enroll = get_object_or_404(TripEnrollment, pk=int(enroll_id))
  context['res'] = trip_enroll
  trip = trip_enroll.trip
  print trip_enroll

  if request.method == 'POST':
    trip_enroll_form = TripEnrollmentForm(request.POST)
    if trip_enroll_form.is_valid():
      for field, val in trip_enroll_form.cleaned_data.items():
        trip_enroll.__dict__[field] = val
      trip_enroll.save()
      return redirect('trips_view', trip_id=trip.id)

    else:
      context['edit_enroll_form'] = trip_enroll_form
  else:
    context['edit_enroll_form'] = TripEnrollmentForm(instance=trip_enroll)

  return render(request, 'trips/trips_enroll_edit.html', context)

"""
 * 
"""
def enrollment_remove(request, enroll_id=None):
  context = {'active':'trips'}
  trip_enroll = get_object_or_404(TripEnrollment, pk=int(enroll_id))
  trip = trip_enroll.trip
  trip_enroll.delete()
  return redirect('trips_view', trip_id=trip.id)




