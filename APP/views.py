from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.contrib import messages
from django.contrib.auth import login
from django.dispatch import receiver

# Create your views here.


def signup(request):
    return render(request, "signup.html")

def profile(request):
    return render(request, "profile.html")

def formhandler(request):
    return render(request, "profile.html")