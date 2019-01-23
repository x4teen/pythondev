from django.http import HttpResponseRedirect
from django.shortcuts import render
from clubmembership.forms import GroupForm
from clubmembership.models import Person, Group, Fee


def add(request):
    form = GroupForm()
    if request.method == 'POST':
        form = GroupForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    return render(request, 'group/add_group.html', {'form': form})


def edit(request, group_id):
    group = Group.objects.get(id=group_id)
    form = GroupForm(instance=group)
    if request.method == 'POST':
        form = GroupForm(request.POST, instance=group)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    return render(request, 'group/edit_group.html', {'form': form, 'id': group_id})


def show(request, group_id):
    group = Group.objects.get(id=group_id)
    members = Person.objects.filter(membership=group_id)
    fees = Fee.objects.filter(group=group_id)
    return render(request, 'group/show_group.html', {'group': group, 'members': members, 'fees': fees})


def delete(request, group_id):
    group = Group.objects.get(id=group_id)
    group.delete()
    return HttpResponseRedirect('/')
