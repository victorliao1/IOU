from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from .forms import MoneyOwedForm, CustomUserCreationForm
from .models import MoneyOwed
def login_page(request):
    return render(request, 'iou_template/login_page.html', {})

def SignUp(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('money_list')
    else:
        form = CustomUserCreationForm()
    return render(request, 'signup.html', {'form': form})

def new_money_owed(request):
    if request.method == "POST":
        form = MoneyOwedForm(request.POST)
        if form.is_valid():
            money_owed = form.save(commit=False)
            money_owed.owner = request.user
            money_owed.save()
            return redirect('money_list')
    else:
        form = MoneyOwedForm()
    return render(request, 'iou_template/front_page.html', {'form' : form})

def money_list(request):
    all_people = MoneyOwed.objects.filter(owner = request.user)
    return render(request, 'iou_template/money_list.html', {'all_people' : all_people})

def deleteEntry(request, entry_id):
    MoneyOwed.objects.get(id=entry_id).delete()
    return HttpResponseRedirect('/moneylist/')
