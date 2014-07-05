from django.shortcuts import render

# Create your views here.
### Mountains index ###
def mountains_home(request):
    
    return render(request, 'mountains/mountains_home.html',{
                    'active':'mountains'
                  })