# django imports
from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from django.contrib import messages
from django.http import Http404
from django.db.models import Q


# model imports
from members.models import Member, Pass, Season
from mountains.models import Mountain, MountainCheckin, MountainScheduleSlot
# other imports
from datetime import datetime
from members.views import get_current_season

### Mountains index ###
"""
 * Display list of mountain links
"""
def mountains_home(request):
    context = {'active':'mountains'}

    mountains = Mountain.objects.all().order_by('name')
    context['mountains'] = mountains
    context['today'] = datetime.strftime(datetime.now().date(), '%Y-%m-%d')
    
    return render(request, 'mountains/mountains_home.html', context)

""" 
 * View the checkins for a mountain overall, or on a day
"""
def mountains_view(request, mountain_abbr=None, date=None)  :
    context = {'active':'mountains'}
    if not date:
	date=datetime.strftime(datetime.now().date(),'%Y-%m-%d')
        return redirect('mountains_view', mountain_abbr=mountain_abbr, date=date)

    mountain = get_object_or_404(Mountain, abbr=mountain_abbr)
    context['mountain'] = mountain
    date = datetime.strptime(date, '%Y-%m-%d').date()
    context['date'] = date
    print 'called'

    all_checkins = MountainCheckin.objects.filter(mountain=mountain)
    # still need to filter for the selected day
    # (Django doesn't let you use model methods in querysets, but list comprehensions do ;)
    checkins = [checkin for checkin in all_checkins if checkin.is_on_day(date) ]
    context['checkins'] = checkins

    # hidden list of active members that user can search on to enroll
    actives = Pass.objects.filter(season=get_current_season()).order_by('active_id')
    context['actives'] = actives
    inactives = Member.objects.filter(~Q(pass__season=get_current_season())).order_by('last_name')
    context['inactives'] = inactives


    return render(request, 'mountains/mountains_view.html', context)

"""
 * Check member pass in at a mountain
"""
def mountains_checkin_add(request, mountain_abbr=None, date=None, active_id=None):
    context = {'active':'mountains'}
    mountain = get_object_or_404(Mountain, abbr=mountain_abbr)
    # make sure mountain is open
    if not mountain.is_open():
        return redirect('mountains_view', mountain_abbr=mountain_abbr, date=date)
    member_pass = get_object_or_404(Pass, active_id=int(active_id), season=get_current_season())

    checkin = MountainCheckin(member_pass=member_pass, mountain=mountain)
    # make sure checkin isn't duplicate
    checkins = mountain.todays_checkins()
    passes = [checkin.member_pass for checkin in checkins]
    if member_pass in passes:
        return redirect('mountains_view', mountain_abbr=mountain_abbr, date=date)
    
    checkin.save()

    return redirect('mountains_view', mountain_abbr=mountain_abbr, date=date)

"""
 * Remove a mountain checkin
"""
def mountains_checkin_remove(request, mountain_abbr=None, date=None, checkin_id=None):
    context = {'active':'mountains'}

    checkin = get_object_or_404(MountainCheckin, pk=int(checkin_id))
    checkin.delete()

    
    return redirect('mountains_view', mountain_abbr=mountain_abbr, date=date)

