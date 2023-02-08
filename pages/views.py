from django.shortcuts import render, redirect
from .models import Member
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


def login_page(request):
    if request.method == "POST":
        email = Member.email
        password = Member.password
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('Member_list/')
        else:
            messages.success(request, ("There was error an error logging in, Try Again!"))
            return redirect('')
    else:
        return render(request, 'login_page.html', {})
def team_member_list(request):
    all_members = Member.objects.all
    member_count = Member.objects.all().count()
    return render(request, 'team_member_list.html', {'all_members':all_members, 'member_count': member_count})

def add_team_member(request):
   return render(request, 'add_team_member.html', {})


def edit_team_member(request):
   return render(request, 'edit_team_member.html', {})

