from django.http import HttpResponseRedirect
from django.shortcuts import render
from clubmembership.forms import PersonForm
from clubmembership.models import Person

actions = {'Home': '/',
           'Add User': '/user/add'}


def add(request):
    form = PersonForm()
    if request.method == 'POST':
        form = PersonForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    return render(request, 'user/add_user.html', {'form': form})


def edit(request, person_id):
    person = Person.objects.get(id=person_id)
    form = PersonForm(instance=person)
    if request.method == 'POST':
        form = PersonForm(request.POST, instance=person)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    return render(request, 'user/edit_user.html', {'form': form, 'id': person_id})


def show(request, person_id):

    person = Person.objects.get(id=person_id)
    actions['Edit User'] = '/user/edit/' + str(person_id)
    actions['Delete User'] = '/user/delete/' + str(person_id)
    return render(request, 'user/show_user.html', {'person': person, 'actions': actions})


def delete(request, person_id):
    user = Person.objects.get(id=person_id)
    user.delete()
    return HttpResponseRedirect('/')


