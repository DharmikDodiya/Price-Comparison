from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login_user/', views.login_user, name='login_user'),
    path('logout_user/', views.logout_user, name='logout_user'),
    path('search_view/', views.search_view, name="search_view"),
    path('search/', views.search, name='search'),
]
