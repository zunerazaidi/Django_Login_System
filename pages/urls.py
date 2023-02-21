from django.urls import path
from django.contrib.auth import views as auth_views

from pages.views.authentication.logout import LogoutView
from pages.views.team_members.add import TeamMemberCreateView
from pages.views.team_members.delete import TeamMemberDeleteView
from pages.views.team_members.edit import TeamMemberUpdateView
from pages.views.team_members.list import TeamMemberListView

urlpatterns = [
    path('login', auth_views.LoginView.as_view(next_page="/"), name='login'),
    path('', TeamMemberListView.as_view(), name='team_member_list'),
    path('register', TeamMemberCreateView.as_view(), name='register'),
    path('logout', LogoutView.as_view(), name='logout'),
    path('<pk>/edit', TeamMemberUpdateView.as_view(), {}, 'edit'),
    path('<pk>/delete/', TeamMemberDeleteView.as_view(), name='delete'),

]
