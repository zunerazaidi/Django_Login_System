from django.http import HttpResponse
from django.shortcuts import render


def login_page(request):
    return render(request, 'login_page.html', {})
def team_member_list(request):
    return render(request, 'team_member_list.html', {})

def add_team_member(request):
   return render(request, 'add_team_member.html', {})


def edit_team_member(request):
   return render(request, 'edit_team_member.html', {})

