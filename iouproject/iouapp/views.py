from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from .forms import MoneyOwedForm, CustomUserCreationForm
from .models import MoneyOwed
from .tables import MoneyOwedTable
from django_tables2 import RequestConfig
from django.conf import settings
from django.urls import reverse
from django.shortcuts import render, get_object_or_404
from paypal.standard.forms import PayPalPaymentsForm
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
def main_page(request):
    return render(request, 'iou_template/main_page.html', {})

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

@login_required
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

# def money_list(request):
#     all_people = MoneyOwed.objects.filter(owner = request.user)
#     return render(request, 'iou_template/money_list.html', {'all_people' : all_people})

@login_required
def deleteEntry(request, entry_id):
    MoneyOwed.objects.get(id=entry_id).delete()
    return HttpResponseRedirect('/moneylist/')

@login_required
@csrf_exempt
def money_list(request):
    table = MoneyOwedTable(MoneyOwed.objects.filter(owner = request.user))
    RequestConfig(request).configure(table)
    host = request.get_host()
    paypal_dict = {
        'business': settings.PAYPAL_RECEIVER_EMAIL ,
        'amount': 100,
        'item_name': 'Item_Name_xyz',
        'invoice': 'Test Payment Invoice',
        'currency_code': 'CAD',
        'notify_url': 'http://{}{}'.format(host, reverse('paypal-ipn')),
        'return_url': 'http://{}{}'.format(host, reverse('payment_done')),
        'cancel_return': 'http://{}{}'.format(host, reverse('payment_canceled')),
       }
    form = PayPalPaymentsForm(initial=paypal_dict)
    return render(request, 'iou_template/money_list.html',{'table': table, 'form': form})

@login_required
@csrf_exempt
def payment_done(request):
    return HttpResponseRedirect('/moneylist/')

@login_required
@csrf_exempt
def payment_canceled(request):
    return render(request, 'payment/payment_cancelled.html')

# @login_required
# @csrf_exempt
# def payment_process(request):
#     return render(request, 'payment/payment_process.html', {'form': form })
