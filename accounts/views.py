from django.http import request
from accounts.models import Profile
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from .models import Profile
from .forms import Login_Form , UserCreationForms , UpdateUserForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

# Create your views here.

def doctors_list(requset):
    doctors = User.objects.all()

    return render(requset, 'user/doctors_list.html', {'doctors':doctors})


def doctors_detail(requset, slug):
    doctors_detail = Profile.objects.get(slug =slug)

    return render(requset, 'user/doctors_detail.html', {'doctors_detail':doctors_detail})



def user_login(request):
    if request.method == 'POST':
        form = Login_Form()
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('accounts:doctors_list')

    else:
        form = Login_Form()
    return render(request, 'user/login.html', {'form':form})


# def signup(request):
#     if request.method == 'POST':
#         from = UserCreationForms(request.POST)
#         if form.is_valid():
#             form.save()
#             username = form.cleaned_data.get('username')
#             password = form.cleaned_data.get('password')
#             user = authenticate(username=username, password=password)
#             login(request, user)
#             return redirect('accounts:doctors_list')

# else:
#     form = UserCreationForms()

# return render(request, 'user/signup.html', {'form':form})



@login_required()
def myprofile(request):

    return render(request, 'user/myprofile.html', {})


def update_profile(request):
    user_form = UpdateUserForm(instance=request.user)

    if request.method == "POST":
        user_form = UpdateUserForm(request.POST, instance=request.user)
        if user_form.is_valid():
            user_form.save()
            return redirect('accounts:doctors_list')

    return render(request, 'user/update_profile.html', {'user_form' : user_form})