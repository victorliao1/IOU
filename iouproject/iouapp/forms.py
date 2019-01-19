from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser, MoneyOwed
from django.forms import ModelForm

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')
    
    class Meta:
        model = CustomUser
        fields = ('username', 'email')


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ('username', 'email')


class MoneyOwedForm(ModelForm):
  
  class Meta:
    model = MoneyOwed
    # fields = '__all__' # Or a list of the fields that you want to include in your form
    fields = ('amount', 'toPerson', 'email',)

