from django.shortcuts import render

# Create your views here.
### Info index ###
def info_home(request):
    
    return render(request, 'info/info_home.html',{
                    'active':'info'
                  })