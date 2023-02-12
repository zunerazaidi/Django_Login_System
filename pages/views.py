from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponseNotFound, HttpResponse

from .forms import CustomUserCreationForm
from .models import MyUser
from django.shortcuts import redirect, render, reverse


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


@login_required
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
                return redirect('/')
    else:
        return HttpResponse('Unauthorized', status=401)
    if not request.user.is_staff_admin:
        form.fields['role'].widget.attrs = {'class':'readonly'}
    context = {'myuser': myuser, 'form': form}
    return render(request, 'registration/edit.html', context)


@login_required
def delete(request, id):
    MyUser.objects.filter(id=id).delete()
    return redirect('/')
