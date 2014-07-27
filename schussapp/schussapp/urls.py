from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

    # Examples:
    # url(r'^$', 'schussapp.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    
### Membership Links (and Home Page) ###    
urlpatterns = patterns('members.views',
    url(r'^$', 'home', name='home'),                           # home page
    url(r'^membership$', 'members_home', name='members_home'),    # membership home page
    url(r'^membership/new$', 'members_new', name='members_new'),  # new members page
    url(r'^membership/view/(?P<id>\d{1,5})$', 'members_view', name='members_view'),  # view members page
    url(r'^membership/view/(?P<id>\d{1,5})/(?P<active_id>\d{1,5})$', 'members_view', name='members_view'),  # view members page with pass num posted
    url(r'^membership/edit/(?P<id>\d{1,5})$', 'members_edit', name='members_edit'),  # edit members page
    url(r'^membership/unenroll/(?P<id>\d{1,5})$', 'members_unenroll_pass', name='members_unenroll_pass'),  # unenroll active member
    url(r'^membership/remove/(?P<id>\d{1,5})$', 'members_remove_member', name='members_remove_member'),  # remove member
    url(r'^membership/lost_stolen/(?P<id>\d{1,5})/(?P<active_id>\d{1,5})$', 'members_lost_stolen', name='members_lost_stolen'),  # lost/stolen a pass
    url(r'^membership/bus_flag/(?P<id>\d{1,5})/(?P<active_id>\d{1,5})$', 'members_bus_flag', name='members_bus_flag'),  # bus flag a pass
    url(r'^membership/pass_flag/(?P<id>\d{1,5})/(?P<active_id>\d{1,5})$', 'members_pass_flag', name='members_pass_flag'),  # flag a pass

)

### Busing Links ###
urlpatterns += patterns('busing.views',
    url(r'^busing$', 'busing_home', name='busing_home'),        # busing home page
    url(r'^busing/(?P<date>(19|20)\d\d[- /.](0[1-9]|1[012])[- /.](0[1-9]|[12][0-9]|3[01]))$', 'busing_home', name='busing_home'),
    url(r'^busing/add$', 'busing_add', name='busing_add'),       # add new bus to system
    url(r'^busing/edit/(?P<id>\d{1,5})$', 'busing_edit', name='busing_edit'),  # edit bus page                        
    url(r'^busing/remove/(?P<id>\d{1,5})$', 'busing_remove', name='busing_remove'),  # remove bus
    url(r'^busing/buscheckin/remove/(?P<id>\d{1,5})$', 'buscheckin_remove', name='buscheckin_remove'),  # remove bus
    url(r'^busing/buscheckin/switch/(?P<res_id>\d{1,5})/(?P<bus_id>\d{1,5})$', 'buscheckin_switch', name='buscheckin_switch'),  # remove bus

)

### Mountain Links ###
urlpatterns += patterns('mountains.views',
    url(r'^mountains$', 'mountains_home', name='mountains_home'), # mountains home page                    
    url(r'^mountains/(?P<mountain_abbr>[a-zA-Z]{1,5})$', 'mountains_view', name='mountains_view'), # view a specific mountain                   
    url(r'^mountains/(?P<mountain_abbr>[a-zA-Z]{1,5})/(?P<date>(19|20)\d\d[- /.](0[1-9]|1[012])[- /.](0[1-9]|[12][0-9]|3[01]))$', 'mountains_view', name='mountains_view'), # view a specific mountain                   
    url(r'^mountains/(?P<mountain_abbr>[a-zA-Z]{1,5})/(?P<date>(19|20)\d\d[- /.](0[1-9]|1[012])[- /.](0[1-9]|[12][0-9]|3[01]))/add-checkin/(?P<active_id>\d{1,5})$', 'mountains_checkin_add', name='mountains_checkin_add'), # checkin a member                   
    url(r'^mountains/(?P<mountain_abbr>[a-zA-Z]{1,5})/(?P<date>(19|20)\d\d[- /.](0[1-9]|1[012])[- /.](0[1-9]|[12][0-9]|3[01]))/remove-checkin/(?P<checkin_id>\d{1,5})$', 'mountains_checkin_remove', name='mountains_checkin_remove'), # delete a checkin                  
             
)

### Events Links ###
urlpatterns += patterns('events.views',
    url(r'^events$', 'events_home', name='events_home'),        # events home page                   
                        
)

### Trip Links ###
urlpatterns += patterns('trips.views',
    url(r'^trips$', 'trips_home', name='trips_home'),           # trips home page
    url(r'^trips/view/(?P<trip_id>\d{1,5})$', 'trips_view', name='trips_view'),  # view a trip page
    url(r'^trips/add$', 'trips_add', name='trips_add'),         # add trip page
    url(r'^trips/edit/(?P<trip_id>\d{1,5})$', 'trips_edit', name='trips_edit'),       # edit a trip page
    url(r'^trips/remove/(?P<trip_id>\d{1,5})$', 'trips_remove', name='trips_remove'),  # remove a trip page
    url(r'^trips/enrollment/add/(?P<pass_id>\d{1,5})/(?P<trip_id>\d{1,5})$', 'enrollment_add', name='enrollment_add'), # edit an trip enrollment
    url(r'^trips/enrollment/edit/(?P<enroll_id>\d{1,5})$', 'enrollment_edit', name='enrollment_edit'), # edit an trip enrollment
    url(r'^trips/enrollment/remove/(?P<enroll_id>\d{1,5})$', 'enrollment_remove', name='enrollment_remove') # remove an trip enrollment
                        
)

### Stats Links ###
urlpatterns += patterns('stats.views',
    url(r'^analytics$', 'stats_home', name='stats_home'),       # analytics home page                    
                        
)

### Information Links ###
urlpatterns += patterns('info.views',
    url(r'^info$', 'info_home', name='info_home'),             # information home page                    
                        
)

### Admin Site and Wiki Site ###
urlpatterns += patterns('',
    url(r'^admin/', include(admin.site.urls)),
    #url(r'^wiki/', include('wakawaka.urls')),
)

