from django.shortcuts import render

from django.http import HttpResponse


def greeting(request):
    return HttpResponse('Hello, World.')


def chinese_greeting(request):
    return HttpResponse('Ni Hao, Shijie.')


def spanish_greeting(request):
    return HttpResponse('Hola, Mundo.')