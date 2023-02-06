from django.urls import path

from . import views

urlpatterns = [
    #path('', views.login_page, name='login_page'),
    path('', views.team_member_list, name='team_member_list'),
    path('add', views.add_team_member, name='add_team_member'),
    path('edit', views.edit_team_member, name='edit_team_member'),
]