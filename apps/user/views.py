from django.shortcuts import render
from django.http import HttpResponse
from django.views import View


# Create your views here.


class RegisterView(View):
    def get(self, request):
        return render(request, 'users/register.html')


class LoginView(View):
    def get(self, request):
        return render(request,'users/login.html')
