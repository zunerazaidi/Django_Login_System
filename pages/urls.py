from django.urls import path

from . import views

urlpatterns = [
    path('', views.TeamMemberList, name='TeamMemberList'),
   # path('AddTeamMember.html', views.AddTeamMember, name='AddTeamMember'),
  #  path('EditTeamMember.html', views.EditTeamMember, name='EditTeamMember'),
]