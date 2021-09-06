from django.urls import path
from django.contrib.auth import views as auth_views
from . import views


app_name = 'accounts'
urlpatterns = [
    path('doctors/', views.doctors_list, name='doctors_list'),
    path('login/', views.user_login, name='login'),
    # path('signup/', views.signup, name='signup'),
    path('myprofile/', views.myprofile, name='myprofile'),
    path('<slug:slug>/', views.doctors_detail, name='doctors_detail'),


]
