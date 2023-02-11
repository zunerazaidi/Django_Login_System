from django.urls import path
from django.contrib.auth import views as auth_views
from . import views


urlpatterns = [
    path('login', auth_views.LoginView.as_view(next_page="/"), name='login'),
    path('', views.team_member_list, name='team_member_list'),
    path('register', views.add_team_member, name='register'),
    path('logout', views.user_logout, name='logout'),
    path(r'^member/edit/(?P<id>\d+)/$', views.edit, {}, 'edit'),
    path(r'^member/delete/(?P<id>\d+)/$', views.delete, {}, 'delete'),
]
