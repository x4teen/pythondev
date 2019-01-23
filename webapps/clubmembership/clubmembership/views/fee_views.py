from django.http import HttpResponseRedirect
from django.shortcuts import render
from clubmembership.forms import FeeForm
from clubmembership.models import Fee


def add(request):
    form = FeeForm
    if request.method == 'POST':
        form = FeeForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    return render(request, 'fee/add_fee.html', {'form': form})


def edit(request, fee_id):
    fee = Fee.objects.get(id=fee_id)
    form = FeeForm(instance=fee)
    if request.method == 'POST':
        form = FeeForm(request.POST, instance=fee)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    return render(request, 'fee/edit_fee.html', {'form': form, 'id': fee_id})


def show(request, fee_id):
    fee = Fee.objects.get(id=fee_id)
    return render(request, 'fee/show_fee.html', {'fee': fee})


def delete(request, fee_id):
    fee = Fee.objects.get(id=fee_id)
    fee.delete()
    return HttpResponseRedirect('/')
