from pages.models import MyUser
from django.shortcuts import render
from django.views import View


class TeamMemberListView(View):
    def get(self, request):
        all_members = MyUser.objects.all
        member_count = MyUser.objects.all().count()
        return render(request, 'team_member_list.html', {'all_members': all_members, 'member_count': member_count})
