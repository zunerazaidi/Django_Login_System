from django.http import HttpResponse
from django.views.generic.edit import CreateView
from pages.forms import CustomUserCreationForm
from pages.models import MyUser


class TeamMemberCreateView(CreateView):
    model = MyUser
    form_class = CustomUserCreationForm
    template_name = 'registration/register.html'
    success_url = "/"

    def get(self, request, *args, **kwargs):
        if not request.user.is_staff_admin:
            return HttpResponse('Unauthorized', status=401)
        else:
            return super().get(request, *args, **kwargs)
