from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from . import views


app_name = 'dashboard'

urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
    path('twitter/', views.twitter, name='twitter'),
    path('twitter/login/', views.twitter_login, name='twitter_login'),
    path('twitter/success/', views.twitter_success, name='twitter_success'),
]