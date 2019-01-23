from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseForbidden, HttpResponseRedirect
from .models import Pet
from .forms import SearchForm, PetForm
from datetime import datetime


def home(request):
    pets = Pet.objects.all()
    return render(request, 'home.html', {'pets': pets})


def pet_detail(request, pet_id):
    try:
        pet = Pet.objects.get(id=pet_id)
    except Pet.DoesNotExist:
        raise Http404('Pet not found')
    return render(request, 'pet_detail.html', {'pet': pet})


def search_something(request):
    form = SearchForm()
    return render(request, 'search_form.html', {"form": form})


def login(request):
    return render(request, 'login.html', {None: None})


def validate_login(request):
    if request.method == "POST":
        user_credential = {'username': request.POST.get('user_name'),
                           'password': request.POST.get('pwd')}
    elif request.method == "GET":
        return HttpResponseForbidden()

    return render(request, 'login_success.html', {'user': user_credential})


def get_pet(request):
    if request.method == 'POST':
        form = PetForm(request.POST,)
        if form.is_valid():
            print('Form is valid')
            form.save(commit=False)
            form.submission_date = datetime.now()
            form.save()
            return HttpResponseRedirect('adoptions:add_pet')
        else:
            return HttpResponse('Form is not valid')
    return render(request, 'get_pet.html', {"form": PetForm()})


def add_pet(request):
    return render(request, 'add_pet.html', {None: None})

