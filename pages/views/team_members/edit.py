from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.views.generic.edit import UpdateView
from pages.forms import CustomUserCreationForm
from pages.models import MyUser
from django.shortcuts import render


class TeamMemberUpdateView(UpdateView):
    model = MyUser
    form_class = CustomUserCreationForm
    template_name = 'registration/edit.html'
    success_url = "/"

    def get(self, request, *args, **kwargs):
        form = self.form_class(instance=MyUser.objects.get(id=self.get_object().id))

        if not (request.user.is_staff_admin or request.user.id == self.get_object().id):
            return HttpResponse('Unauthorized', status=401)
        else:
            if not request.user.is_staff_admin:
                form.fields['role'].widget.attrs = {'class': 'readonly'}
            return render(request, self.template_name, {'form': form, 'myuser': self.get_object()})

    def post(self, request, *args, **kwargs):
        my_user = self.get_object()
        # We do not want to log out the current user if they update their own information
        if my_user.id == request.user.id:
            authenticate(username=my_user.email, password=my_user.password)
            login(request, my_user)
        return super().post(request, *args, **kwargs)
