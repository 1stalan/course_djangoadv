from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.contrib.auth.views import LogoutView


def home(request):
    return render(request, 'home/home.html')

class MyLogout(LoginRequiredMixin, LogoutView):
    template_name = 'home/home.html'






