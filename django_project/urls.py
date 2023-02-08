from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
   # path("login/", include('django.contrib.auth.urls')),
    path("", include('pages.urls')),
]
