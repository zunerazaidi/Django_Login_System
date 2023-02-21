from django.views.generic.edit import DeleteView
from pages.models import MyUser
from django.http import HttpResponse


class TeamMemberDeleteView(DeleteView):
    model = MyUser
    success_url = "/"
    template_name = 'registration/delete.html'

    def get(self, request, *args, **kwargs):
        if not (request.user.is_staff_admin or request.user.id == self.get_object().id):
            return HttpResponse('Unauthorized', status=401)
        else:
            return super().post(request, *args, **kwargs)
