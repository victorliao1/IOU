from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic

def login_page(request):
    return render(request, 'iou_template/login_page.html', {})

def front_page(request):
    return render(request, 'iou_template/front_page.html', {})

class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'
