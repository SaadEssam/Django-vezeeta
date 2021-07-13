from django.urls import path
from . import views


app_name = 'accounts'
urlpatterns = [
    path('doctor/', views.doctors_list, name='doctors_list'),
    path('<slug:slug>/', views.doctors_detail, name='doctors_detail'),


]
