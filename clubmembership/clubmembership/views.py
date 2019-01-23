from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render
from datetime import datetime
from .forms import PersonForm, GroupForm
from .models import Person, Group


def home_page(request):
    persons = Person.objects.order_by('name')
    groups = Group.objects.order_by('name')
    return render(request, 'home_page.html', {'persons': persons, 'groups': groups})


def add_user(request):
    form = PersonForm()
    if request.method == 'POST':
        form = PersonForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    return render(request, 'add_user.html', {'form': form})


def add_group(request):
    form = GroupForm()
    if request.method == 'POST':
        form = GroupForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    return render(request, 'add_group.html', {'form': form})


def edit_user(request, person_id):
    person = Person.objects.get(id=person_id)
    form = PersonForm(instance=person)
    if request.method == 'POST':
        form = PersonForm(request.POST, instance=person)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    return render(request, 'edit_user.html', {'form': form, 'id': person_id})


def edit_group(request, group_id):
    group = Group.objects.get(id=group_id)
    form = GroupForm(instance=group)
    if request.method == 'POST':
        form = GroupForm(request.POST, instance=group)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    return render(request, 'edit_group.html', {'form': form, 'id': group_id})


def delete_user(request, person_id):
    user = Person.objects.get(id=person_id)
    user.delete()
    return HttpResponseRedirect('/')


def delete_group(request, group_id):
    group = Group.objects.get(id=group_id)
    group.delete()
    return HttpResponseRedirect('/')
