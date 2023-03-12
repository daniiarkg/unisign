from django.shortcuts import render, HttpResponse, redirect
from django.http import HttpResponseNotFound
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.utils.crypto import get_random_string as rans
from .models import *
from .forms import *


def log_in(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            c = Citizen.objects.get(phone=form.cleaned_data['phone'])
            login(request, c.user)
            return redirect('main')
    else:
        form = LoginForm()
    return render(request, 'main/login.html', {'f': form})


def register(request):
    try:
        if request.method == 'POST':
            form = RegisterForm(request.POST)
            if form.is_valid():
                gb = rans(length=32)
                while User.objects.filter(username=gb):
                    gb = rans(length=32)
                f = form.cleaned_data
                u = User.objects.create_user(
                    username=gb, password=f['password'], first_name=f['first_name'], last_name=f['last_name'])
                c = Citizen(user=u, pin=f['pin'], phone=f['phone']).save()
                login(request, u)
                return redirect('main')
        else:
            form = RegisterForm()
        return render(request, 'main/register.html', {'f': form})
    except:
        return HttpResponseNotFound()


def search_res(request):
    if request.method == 'POST':
        form = PetitionSearchForm(request.POST)
        if form.is_valid():
            p = Petition.objects.filter(
                title__contains=form.cleaned_data['title'])
            return render(request, 'main/results.html', {'o': p})
        else:
            return HttpResponseNotFound()
    else:
        return HttpResponseNotFound()


def reg_petition(request, id):
    p = Petition.objects.get(id=id)
    p.votes += 1
    p.save()
    return render(request, 'main/sub.html', {})


def view_petition(request, id):
    p = Petition.objects.get(id=id)
    return render(request, 'main/view.html', {'p': p})


@ login_required(login_url='login/')
def create_petition(request):
    if request.method == 'POST':
        print(request.user)
        pet = Petition(author=Citizen.objects.get(user=request.user))
        form = PetitionForm(request.POST, request.FILES, instance=pet)
        if form.is_valid():
            form.save()
            return redirect('view_petition', pet.id)
    else:
        form = PetitionForm()
    return render(request, 'main/create.html', {'f': form})


def main(request):
    return render(request, 'main/index.html', {'o': Petition.objects.all().order_by('votes')})
