from django.http import HttpResponse
from django.shortcuts import render


def team_member_list(request):
    #return HttpResponse("Hello, I am zunera")
    return render(request, 'team_member_list.html', {})

#def AddTeamMember(request):
 #   return render(request, 'AddTeamMember.html', {})


#def EditTeamMember(request):
 #   return render(request, 'EditTeamMember.html', {})

