from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.contrib import messages
from django.contrib.auth import login
from django.dispatch import receiver
from django.template.context_processors import request
# import UserProfile
from APP.forms import SignupForm
from APP.models import UserProfile

# Create your views here.


def signup(request):
    return render(request, "signup.html", {'signupform':SignupForm()})

def profile(request):
    return render(request, "profile.html")

def formhandler(request):
    if request.POST and request.FILES:
        form = SignupForm(request.POST, request.FILES)
        if form.is_valid():
            
            return HttpResponse("FILES and POST")
        return HttpResponse(f"Invalid {form.errors}")