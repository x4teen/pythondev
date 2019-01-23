from django.shortcuts import render
from clubmembership.models import Person, Group


def home_page(request):
    persons = Person.objects.order_by('name')
    groups = Group.objects.order_by('name')
    return render(request, 'home_page.html', {'persons': persons, 'groups': groups})

