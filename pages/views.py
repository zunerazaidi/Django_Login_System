from django.http import HttpResponse
from django.shortcuts import render


def TeamMemberList(request):
    #return HttpResponse("Hello, I am zunera")
    return render(request, 'TeamMemberList.html', {})

#def AddTeamMember(request):
 #   return render(request, 'AddTeamMember.html', {})


#def EditTeamMember(request):
 #   return render(request, 'EditTeamMember.html', {})

