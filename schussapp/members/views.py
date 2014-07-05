# django imports
from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from django.contrib import messages
from django.http import Http404

# model imports
from members.models import Member, Pass, Season

# other imports
from datetime import datetime, date

# form imports
from members.forms import NewMemberForm, EditMemberForm, LostStolenForm, BusFlagForm, PassFlagForm

# This file tells Django how to actually render the pages for all membership pages
### HOMEPAGE FOR WHOLE SITE ###
def home(request):
    
    return render(request, 'home.html',{
                    'active':'home'
                  })

### HOMEPAGE FOR MEMBERS ###
def members_home(request):
    context = { 'active':'members' }
    context['filter_list'] = Member.objects.all().order_by('last_name')
    print context['filter_list']

    return render(request, 'members/members_home.html', context)

"""
* Generate and display a form for creating and signing up a new member
"""
def members_new(request):
    context = { 'active':'members' }
    context['filter_list'] = Member.objects.all().order_by('last_name')
    print context['filter_list']

    # if form was submitted
    if (request.method == 'POST'):
        new_member_form = NewMemberForm(request.POST)
        if new_member_form.is_valid(): #all validation rules pass
            member_id = create_new_member_and_pass( new_member_form.cleaned_data )
            
            new_member_form = NewMemberForm( new_member_form.cleaned_data )
            context['new_member_form'] = new_member_form
            return redirect('members_view', id=member_id)
        else:
            context['new_member_form'] = new_member_form
            return render(request, 'members/members_new.html', context)
    else:
        new_member_form = NewMemberForm()
        context['new_member_form'] = new_member_form
        return render(request, 'members/members_new.html', context)

"""
* Display the information about a given member
"""
def members_view(request, id="1", active_id=None):
    context = { 'active':'members' }
    context['filter_list'] = Member.objects.all().order_by('last_name')
    
    id = int(id)
    # error if member doesn't exist
    print id
    member = get_object_or_404(Member, pk=id)
    print member
    context['member'] = member

    # if we're asking for specific active id, use that one (must be current though)
    if(active_id):
        pass_set = member.pass_set.filter(active_id=active_id, season=get_current_season())
        # if the pass num we asked for doesnt exist, error out
        if not pass_set:
            raise Http404
        # if we have more than one pass with that id, the most recent will be used
        member_pass = pass_set[0]
        context['pass'] = member_pass
        # find the verbose name of that type
        member_type = get_verbose_choice(member_pass.member_type , NewMemberForm.TYPE_CHOICES)
        context['verbose_member_type'] = member_type[0]
        context['verbose_member_subtype'] = member_type[1]
        
    # if we didn't ask for a pass number, get this years if it exists
    else:
        pass_set = member.pass_set.filter(season=get_current_season())
        # if the member has an active pass
        if pass_set:
            member_pass = pass_set[0]
            context['pass'] = member_pass
            # find the verbose name of that type
            member_type = get_verbose_choice(member_pass.member_type , NewMemberForm.TYPE_CHOICES)
            context['verbose_member_type'] = member_type[0]
            context['verbose_member_subtype'] = member_type[1]
        # else we never found a pass for this year and the member is inactive
        else:
            context['verbose_member_type'] = 'Inactive'

    # get the verbose dorm name, if it exists
    dorm = get_verbose_choice(member.dorm , NewMemberForm.DORM_CHOICES)
    if (dorm[0]):
        verbose_dorm = dorm[0]  + " - " + dorm[1]
        context['verbose_dorm_type'] = verbose_dorm
    else: context['verbose_dorm_type'] = 'None'
    # generate a verbose gender name (because the 'get_verbose_choice' isn't robust enough)
    if( member.gender == 'M'): gender = 'Male'
    else: gender = 'Female'
    context['verbose_gender'] = gender
     
    return render(request, 'members/members_view.html', context)

"""
* Edit the information about a given member
"""
def members_edit(request, id="1"):
    context = { 'active':'members' }
    context['filter_list'] = Member.objects.all().order_by('last_name')
    id=int(id)
    context['member_id'] = id
    # if form was submitted
    if (request.method == 'POST'):
        edit_member_form = EditMemberForm(request.POST)
        if edit_member_form.is_valid(): #all validation rules pass
            edit_member_and_pass( edit_member_form.cleaned_data )
            member_id = edit_member_form.cleaned_data['member_id']
            return redirect('members_view', id=member_id)
        else:
            context['edit_member_form'] = edit_member_form
            #return render(request, 'members/members_edit.html', context)
    # else display an initial form
    else:
        member = get_object_or_404(Member, pk=id)
        # if we find the member
        member_dict = { k:v for k,v in member.__dict__.items() if k not in ['_state', 'photo']}
        member_dict['member_id'] = id
        # get only their passes for this season, that haven't been flagged lost/stolen
        pass_set = member.pass_set.filter(season=get_current_season(), lost_stolen=False)
        # if the member has one current season pass associated with him
        if ( len(pass_set) == 1):
            member_pass = pass_set[0]
            member_dict['member_type'] = member_pass.member_type
            member_dict['active_id'] = member_pass.active_id
            edit_member_form = EditMemberForm( member_dict)
            context['edit_member_form'] = edit_member_form
        # make sure they don't have too many for some crazy reason
        elif ( len(pass_set) > 1 ):
            context['pass_error'] = True
            context['pass_error_msg'] = 'Error: Member has too many active passes for this season.\nPlease have a director edit this record directly.'
        # else the member hasn't been enrolled yet for this season
        # so we want to reenroll them
        else:
            edit_member_form = EditMemberForm( member_dict )
            context['edit_member_form'] = edit_member_form
    return render(request, 'members/members_edit.html', context)

"""
* Unenroll member from this seasons pass, if the pass exists
* But don't delete the member
"""
def members_unenroll_pass(request, id="1"):
    context = { 'active':'members' }
    context['filter_list'] = Member.objects.all().order_by('last_name')
    id=int(id)
    member = get_object_or_404( Member, pk=id)
    context['member'] = member
    current_pass = member.pass_set.filter(season=get_current_season, lost_stolen=False)
    if not current_pass:
        raise Http404
    context['active_id'] = current_pass[0].active_id
    current_pass.delete()
    
    return render(request, 'members/members_unenroll.html', context)
    
"""
* Take in member id and remove the member AND pass instances associated with it
* NOTE: This DOES edit the database
"""
def members_remove_member(request, id="1" ):
    context = { 'active':'members' }
    context['filter_list'] = Member.objects.all().order_by('last_name')
    id=int(id)
    member = get_object_or_404(Member, pk=id)
    context['first_name'] = member.first_name
    context['last_name'] = member.last_name
    member.delete()
    return render(request, 'members/members_remove.html', context)

"""
* Take in member id and pass number and display or complete the lost/stolen form associated with it
* NOTE: This DOES edit the database
"""
def members_lost_stolen(request, id="1", active_id=None ):
    context = { 'active':'members' }
    context['filter_list'] = Member.objects.all().order_by('last_name')
    id=int(id)
    member = get_object_or_404(Member, pk=id)
    context['member'] = member
    context['first_name'] = member.first_name
    context['last_name'] = member.last_name
    # if the form was submitted
    if ( request.method == 'POST' ):
        lost_stolen_form = LostStolenForm(request.POST)
        # set the members pass to 
        if(lost_stolen_form.is_valid()):
            member_pass_set = member.pass_set.filter(season=get_current_season(), active_id=active_id, lost_stolen=False)
            if not member_pass_set:
                raise Http404
            member_pass = member_pass_set[0]
            member_pass.lost_stolen = True
            member_pass.lost_stolen_note = lost_stolen_form.cleaned_data['lost_stolen_note']
            member_pass.save()
            
            # make the new pass and assign it to the member
            pass_set = Pass.objects.filter(season=get_current_season(), active_id__gte=26)
            active_set = { p.active_id for p in pass_set}
            if ( len(active_set) == 0 ): active_id = 26 # first non-reserved member of the season
            else:
                active_range = range(26, max(active_set))
                active_id = max(active_set) + 1 # set to the max + 1
                # unless we find an empty space
                for i in active_range:
                    if i not in active_set: # if we find one in the range, but not in the set
                        active_id = i # use that empty space
                        break       
            new_pass = Pass( member=member, season=get_current_season(),
                                  active_id=active_id, is_reserved=False,
                                  member_type=member_pass.member_type)
            new_pass.save()
            context['pass'] = new_pass
            
        else:
            context['lost_stolen_form'] = lost_stolen_form
    else:
        context['lost_stolen_form'] = LostStolenForm()
    return render(request, 'members/members_lost_stolen.html', context)
    
"""
* Take in member id and pass number and display or complete the bus_flag form associated with it
* NOTE: This DOES edit the database
"""
def members_bus_flag(request, id="1", active_id=None ):
    context = { 'active':'members' }
    context['filter_list'] = Member.objects.all().order_by('last_name')
    id=int(id)
    member = get_object_or_404(Member, pk=id)
    context['first_name'] = member.first_name
    context['last_name'] = member.last_name
    # get the pass in question, bailing if it doesn't exist
    member_pass_set = member.pass_set.filter(season=get_current_season(), active_id=active_id)
    if not member_pass_set:
        raise Http404
    member_pass = member_pass_set[0]
    context['member'] = member
    context['pass'] = member_pass
    # if the form was submitted
    if ( request.method == 'POST' ):
        bus_flag_form = BusFlagForm(request.POST)
        # set the members pass to 
        if(bus_flag_form.is_valid()):
            
            member_pass.bus_flag = True
            member_pass.bus_flag_note = bus_flag_form.cleaned_data['bus_flag_note']
            member_pass.save()
            
        else:
            context['bus_flag_form'] = bus_flag_form
            
    # if it's already flagged, then we clicked the remove flag link
    elif member_pass.bus_flag:
        member_pass.bus_flag = False
        member_pass.bus_flag_note = ""
        member_pass.save()
        context['removed_flag'] = True
    # else render the blank form
    else:
        context['bus_flag_form'] = BusFlagForm()
    return render(request, 'members/members_bus_flag.html', context)

"""
* Take in member id and pass number and display or complete the pass_flag form associated with it
* NOTE: This DOES edit the database
"""
def members_pass_flag(request, id="1", active_id=None ):
    context = { 'active':'members' }
    context['filter_list'] = Member.objects.all().order_by('last_name')
    id=int(id)
    member = get_object_or_404(Member, pk=id)
    context['first_name'] = member.first_name
    context['last_name'] = member.last_name
    # get the pass in question, bailing if it doesn't exist
    member_pass_set = member.pass_set.filter(season=get_current_season(), active_id=active_id)
    if not member_pass_set:
        raise Http404
    member_pass = member_pass_set[0]
    context['member'] = member
    context['pass'] = member_pass
    # if the form was submitted
    if ( request.method == 'POST' ):
        pass_flag_form = PassFlagForm(request.POST)
        # set the members pass to 
        if(pass_flag_form.is_valid()):
            
            member_pass.pass_flag = True
            member_pass.pass_flag_note = pass_flag_form.cleaned_data['pass_flag_note']
            member_pass.save()
            
        else:
            context['pass_flag_form'] = pass_flag_form
            
    # if it's already flagged, then we clicked the remove flag link
    elif member_pass.pass_flag:
        member_pass.pass_flag = False
        member_pass.pass_flag_note = ""
        member_pass.save()
        context['removed_flag'] = True
    # else render the blank form
    else:
        context['pass_flag_form'] = PassFlagForm()
    return render(request, 'members/members_pass_flag.html', context)

"""
=================================================================================
* Helper functions
* These are not actual views and are only used by other member-relevant views
=================================================================================
"""
"""
* Take in a cleaned new member form and create a member instance
* and create a pass with the current season and associate it with the member
* NOTE: This DOES edit the database
"""
def create_new_member_and_pass( clean_new_member_data ):
    ### Create the Member Instance ###
    # create the dictionary of attributes relevant to the member model
    member_dict = {k:v for k,v in clean_new_member_data.items() if k not in ['member_type', 'is_reserved', 'reserved_id']}
    #print member_dict
    member = Member( **member_dict )
    member.save()
    
    ### Create the Pass instance ###
    current_season = get_current_season()
    is_reserved = clean_new_member_data['is_reserved']
    # if signed up as reserved, use that reserved id
    if ( is_reserved ):
        active_id = clean_new_member_data['reserved_id']
    # else give them the lowest active id for the season, which is greater than 25
    # this should fill in holes if someone gets deleted
    else:
        pass_set = Pass.objects.filter(season=current_season, active_id__gte=26)
        active_set = { p.active_id for p in pass_set}
        if ( len(active_set) == 0 ): active_id = 26 # first non-reserved member of the season
        else:
            active_range = range(26, max(active_set))
            active_id = max(active_set) + 1 # set to the max + 1
            # unless we find an empty space
            for i in active_range:
                if i not in active_set: # if we find one in the range, but not in the set
                    active_id = i # use that empty space
                    break
    
    member_pass = Pass( member=member, season=current_season,
                        active_id=active_id, is_reserved=is_reserved,
                        member_type=clean_new_member_data['member_type'] )
    # add them to the database
    member_pass.save()
  
    return member.id
"""
* Take in a cleaned existing member form and edit the member and pass instance associated with it
* NOTE: This DOES edit the database
"""
def edit_member_and_pass( clean_edit_member_data ):
    ### Create the Member Instance ###
    # create the dictionary of attributes relevant to the member model
    print '1', clean_edit_member_data.items()
    member_dict = {k:v for k,v in clean_edit_member_data.items() if k not in ['member_type', 'member_id', 'active_id', 'is_reserved', 'reserved_id']}
    #print member_dict
    member = Member.objects.get(pk=int(clean_edit_member_data['member_id']))
    member.__dict__.update(member_dict)
    member.save()
    
    ### Edit or Create the Pass instance ###
    member_pass_set = member.pass_set.filter(season=get_current_season(),lost_stolen=False)
    if (len(member_pass_set) == 1 ):
        member_pass = member_pass_set[0]
        member_pass.member_type = clean_edit_member_data['member_type']
        member_pass.save()
    elif (len(member_pass_set) > 1):
        # TODO: Break for too many current passes
        # for now just bail out gracefully
        return
    # else the member doesn't have a pass yet for this season
    else:
        ### Create the Pass instance ###
        current_season = get_current_season()
        is_reserved = clean_edit_member_data['is_reserved']
        # if signed up as reserved, use that reserved id
        if ( is_reserved ):
            active_id = clean_edit_member_data['reserved_id']
        # else give them the lowest active id for the season, which is greater than 25
        # this should fill in holes if someone gets deleted
        else:
            pass_set = Pass.objects.filter(season=current_season, active_id__gte=26)
            active_set = { p.active_id for p in pass_set}
            if ( len(active_set) == 0 ): active_id = 26 # first non-reserved member of the season
            else:
                active_range = range(26, max(active_set))
                active_id = max(active_set) + 1 # set to the max + 1
                # unless we find an empty space
                for i in active_range:
                    if i not in active_set: # if we find one in the range, but not in the set
                        active_id = i # use that empty space
                        break
        
        member_pass = Pass( member=member, season=current_season,
                            active_id=active_id, is_reserved=is_reserved,
                            member_type=clean_edit_member_data['member_type'] )
        # add them to the database
        member_pass.save()
  

    

"""
* Returns the latest Season, and makes sure that season is actually current
"""
def get_current_season():
    seasons = Season.objects.order_by('-spring')
    for season in seasons:
        if season.is_current():
            return season
    
"""
* Converts member type attribute short version into verbose text for display
* Currently this is pretty hacked up, and only works with the DORM and MEMBER choice lists
* But it will error out on the GENDER list because "M" and "F" don't have a value at [1]
* So be careful about using it, it's error prone...
* TODO: Make this robust
"""
def get_verbose_choice( short_name , choices ):
    verbose_name = ''
    prefix = ''
    suffix = ''
    for meta_choice in choices:
        for choice in meta_choice[1]:
            if(choice[0] == short_name):
                prefix = meta_choice[0]
                if(len(choice) > 1): suffix = choice[1]
        if (meta_choice[0] == short_name):
            prefix = meta_choice[1]
    verbose_name = (prefix, suffix)        
    return verbose_name
        