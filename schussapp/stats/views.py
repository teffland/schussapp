from django.shortcuts import render

# Create your views here.
### Stats index ###
def stats_home(request):
    
    return render(request, 'stats/stats_home.html',{
                    'active':'stats'
                  })