from django.shortcuts import render
import csv
from django.http import HttpResponse
from members.models import Member, Pass, Season
from members.views import get_current_season
# Create your views here.
### Analytics index ###
def analytics_home(request):
    
    return render(request, 'analytics/analytics_home.html',{
                    'active':'analytics'
                  })

"""
* Query DB and return all of this years Member Emails
"""
def export_member_emails(request):
    # set up csv file response
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="member_emails.csv"'
  
    # get active members
    actives = Pass.objects.filter(season=get_current_season()).order_by('active_id')
    # write out csv
    writer = csv.writer(response)
    writer.writerow(["First Name", "Last Name", "Active ID", "Membership Type", "Email"])
    for m_pass in actives:
        member = m_pass.member
        first_name = member.first_name
        last_name = member.last_name
        pass_num = m_pass.active_id
        m_type = m_pass.member_type
        email = m_pass.member.email
        writer.writerow([first_name, last_name, pass_num, m_type, email])

    return response
