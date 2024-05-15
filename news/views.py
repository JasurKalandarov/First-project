from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def home(request):
    return HttpResponse(f'Hello, My home'
                        f"<img src='https://t3.ftcdn.net/jpg/06/14/84/58/360_F_614845842_pNcPaSxVwBiO6hGaaSXKrQOCs6xqnijX.jpg'>")


def home1(request):
    return HttpResponse('Welcome to My sayt!!!')