from django.http import HttpResponse
from django.shortcuts import render
from .models import Member



def login_page(request):
    return render(request, 'login_page.html', {})
def team_member_list(request):
    all_members = Member.objects.all
    member_count = Member.objects.all().count()
    return render(request, 'team_member_list.html', {'all_members':all_members, 'member_count': member_count})

def add_team_member(request):
   return render(request, 'add_team_member.html', {})


def edit_team_member(request):
   return render(request, 'edit_team_member.html', {})

