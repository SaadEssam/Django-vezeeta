from django.urls import path
from . import views


app_name = 'accounts'
urlpatterns = [
    path('doctors/', views.doctors_list, name='doctors_list'),
    path('login/', views.user_login, name='login'),
    path('<slug:slug>/', views.doctors_detail, name='doctors_detail'),


]
