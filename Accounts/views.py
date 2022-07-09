import random

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
import requests
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from Accounts.models import Profile
from django.urls import reverse
from Accounts.forms import SignUpForm,EditProfile


def sing_up(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            age = form.cleaned_data.get('age')
            user = authenticate(request, username=username, password=password)
            login(request, user)
            profile = Profile.objects.get_or_create(user=request.user, username_id=username, age=age)
            return HttpResponseRedirect(reverse('Chats:test'))
    else:
        form = SignUpForm()
    context = {'form': form}
    return render(request, 'Accounts/sign_up.html', context)


def login_view(request):
    context = {

    }
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is None:
            context['error'] = 'username or password is wrong'
            return render(request, 'accounts/login.html', context)
        else:
            login(request, user)
            return HttpResponseRedirect(reverse('Chats:test'))

    else:
        return render(request, 'accounts/login.html', context)


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('Account:login'))



def edit_sign(request):
    profile1 = request.user.profile
    context = {
        'profile1': profile1
    }
    if request.method == 'POST':

        profile = EditProfile(request.POST, files=request.FILES, instance=request.user.profile)

        if profile.is_valid():
            profile.save()
            return HttpResponseRedirect(reverse('Account:profile_detail'))

    else:
        profile = EditProfile(instance=request.user.profile)

    context['profile'] = profile
    return render(request, 'Accounts/profile.html', context)
