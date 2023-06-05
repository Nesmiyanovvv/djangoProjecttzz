from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.http import HttpResponse
import requests


def vk_auth_login(request):
    # код авторизации ВКонтакте

    # Сохранение данных пользователя в сессии
    request.session['first_name'] = first_name
    request.session['photo_200'] = photo_200

    # Редирект на другую страницу
    return redirect('profile')
def main(request):
    return render(request, 'main.html')

def profile(request):
    return render(request, 'profile.html')