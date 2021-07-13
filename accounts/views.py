from accounts.models import Profile
from django.shortcuts import render
from django.contrib.auth.models import User
from .models import Profile

# Create your views here.

def doctors_list(requset):
    doctors = User.objects.all()

    return render(requset, 'user/doctors_list.html', {'doctors':doctors})


def doctors_detail(requset, slug):
    doctors_detail = Profile.objects.get(slug =slug)

    return render(requset, 'user/doctors_detail.html', {'doctors_detail':doctors_detail})