from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.messages import constants as messages
from django.contrib import messages
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse, Http404, HttpResponseNotAllowed
from .forms import *
from .models import *


# Create your views here.
def home(request):

    context = {}
    return render(request, 'index.html', context)

def registration(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            first_name = form.cleaned_data.get('username')
            messages.success(
                request, first_name + ' ' + 'your account was created successfully!')
            return redirect('login')
    else:
        form = SignUpForm()

    context = {
        'form': form
    }
    return render(request, 'auth/registration.html', context)


def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username,
                            password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'Logged in as' + ' ' + username)

            return redirect('moringa')
        else:
            messages.error(request, 'Invalid Username or Password')

    context = {}
    return render(request, 'auth/login.html', context)


def logoutUser(request):
    logout(request)
    messages.info(
        request, 'You have logged out. Log back in to update schedule.')
    return redirect('login')


def moringa(request):
    current_user = request.user
    

    context = {
               'current_user': current_user,
               }
    return render(request, 'moringa.html', context)

def others(request):
    users = Moringa.objects.all()
    context = {'users': users}
    return render(request, 'others.html', context)
