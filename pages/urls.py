from django.urls import path

from . import views

from .views import profile_view, spotify_view

app_name= 'pages'

urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    path('accounts/profile/', profile_view, name='account_profile'),
    path('spotify', spotify_view, name='spotify_view'),
]