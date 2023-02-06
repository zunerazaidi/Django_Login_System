from django.urls import path

from . import views

urlpatterns = [
    path('', views.team_member_list, name='team_member_list'),
   # path('AddTeamMember.html', views.AddTeamMember, name='AddTeamMember'),
  #  path('EditTeamMember.html', views.EditTeamMember, name='EditTeamMember'),
]