from django.shortcuts import render
from django.contrib.auth.models import User

# Create your views here.

def doctors_list(requset):
    doctors = User.objects.all()

    return render(requset, 'user/doctors_list.html', {'doctors':doctors})
