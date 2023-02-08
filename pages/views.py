from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from .models import Member
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


def login_page(request):
    if request.method == "POST":
        user = authenticate(username=request.POST['username'], password=request.POST['password'])
        if user is not None:
            login(request, user)
            return redirect('member_list/')
        else:
            messages.success(request, ("There was error an error logging in, Try Again!"))
            return HttpResponseRedirect(request.path_info)
    else:
        return render(request, 'login_page.html', {})

def signout(request):
    pass
def team_member_list(request):
    all_members = Member.objects.all
    member_count = Member.objects.all().count()
    return render(request, 'team_member_list.html', {'all_members':all_members, 'member_count': member_count})

def add_team_member(request):
   return render(request, 'add_team_member.html', {})


def edit_team_member(request):
   return render(request, 'edit_team_member.html', {})

