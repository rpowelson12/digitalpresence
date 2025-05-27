from django.contrib import admin
from django.urls import path, include

from . import views

app_name = 'digital_presence'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('accounts.urls')),
    path('', include('core.urls')),
    path("__reload__/", include("django_browser_reload.urls")),
]
