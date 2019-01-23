from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    response = '<html><body>'
    response += '<h1> Welcome to My Blog </h1>'
    response += '</body></html>'
    return HttpResponse(response)


def show_request(request):
    response = '<html><body>'
    response += '<h1> Available Methods on Request </h1>'
    response += '<ol>'
    methods = dir(request)

    for method in methods:
        response += '<li>' + str(method) + '</li>'

    response += '</ol>'
    response += '</body></html>'
    return HttpResponse(response)


def show_response(request):
    response = '<html><body>'
    response += '<h1> Available Methods on Response </h1>'
    response += '<ol>'
    methods = dir(HttpResponse())

    for method in methods:
        response += '<li>' + str(method) + '</li>'

    response += '</ol>'
    response += '</body></html>'
    return HttpResponse(response)