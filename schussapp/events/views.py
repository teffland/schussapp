from django.shortcuts import render

# Create your views here.
### Events index ###
def events_home(request):
    
    return render(request, 'events/events_home.html',{
                    'active':'events'
                  })