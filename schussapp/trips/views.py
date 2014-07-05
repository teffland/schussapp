from django.shortcuts import render

# Create your views here.
### Bus index ###
def trips_home(request):
    
    return render(request, 'trips/trips_home.html',{
                    'active':'trips'
                  })