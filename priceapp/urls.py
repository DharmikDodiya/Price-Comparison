from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_user, name='home'),
    path('login_user/', views.login_user, name='login_user'),
    path('logout_user/', views.logout_user, name='logout_user'),
    path('search_view/', views.search_view, name="search_view"),
    path('search/', views.search, name='search'),
    path("products/", views.product_list, name="product_list"),
    path('register/', views.register_user, name='register_user'),
]

