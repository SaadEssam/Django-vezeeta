from django.shortcuts import render

# Create your views here.

def app(requset):
    return render(requset, 'user/app.html', {})
