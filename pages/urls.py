from django.urls import path
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    path('login', auth_views.LoginView.as_view(next_page=""), name='login'),
    path('', views.team_member_list, name='team_member_list'),

    # path('member/add', auth_views.LoginView.as_view()),
    # path('member/edit', auth_views.LoginView.as_view()),

    # path('', views.login_page, name='login'),
    # path('add', views.add_team_member, name='add_team_member'),
    # path('edit', views.edit_team_member, name='edit_team_member'),
]