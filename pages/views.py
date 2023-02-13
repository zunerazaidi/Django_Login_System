from django.contrib.auth import logout, authenticate, login
from django.http import HttpResponseRedirect, HttpResponse

from .forms import CustomUserCreationForm
from .models import MyUser
from django.shortcuts import redirect, render


def team_member_list(request):
    all_members = MyUser.objects.all
    member_count = MyUser.objects.all().count()
    return render(request, 'team_member_list.html', {'all_members': all_members, 'member_count': member_count})


def add_team_member(request):
    if request.user.is_staff_admin:
        if request.method == 'POST':
            form = CustomUserCreationForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('/')
        else:
            form = CustomUserCreationForm()
        return render(request, 'registration/register.html', {'form': form})
    else:
        return redirect('/')

def user_logout(request):
    logout(request)
    return HttpResponseRedirect("logout")


def edit(request, id):
    id = int(id)
    myuser = MyUser.objects.get(id=id)
    if request.user.is_staff_admin or request.user.id == id:
        if request.method != 'POST':
            form = CustomUserCreationForm(instance=myuser)
        else:
            form = CustomUserCreationForm(request.POST, request.FILES, instance=myuser)
            if form.is_valid():
                form.save()

                # We do not want to log out the current user if they update their own information
                if myuser.id == request.user.id:
                    authenticate(username=myuser.email, password=myuser.password)
                    login(request, myuser)
                return redirect('/')
    else:
        return HttpResponse('Unauthorized', status=401)
    if not request.user.is_staff_admin:
        form.fields['role'].widget.attrs = {'class':'readonly'}
    context = {'myuser': myuser, 'form': form}
    return render(request, 'registration/edit.html', context)


def delete(request, id):
    MyUser.objects.filter(id=id).delete()
    return redirect('/')
