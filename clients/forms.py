from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import University, Agent, Contact, Subscribe

class UniversityForm(ModelForm):
  name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','required':'required'}))
  address = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'required':'required'}))
  city = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','required':'required'}))
  state = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','required':'required'}))
  postal = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','required':'required'}))
  country = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','required':'required'}))
  website = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','required':'required'}))
  email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control','required':'required'}))
  description = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','required':'required'}))
  isono = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','required':'required'}))
  representative = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','required':'required'}))
  position = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','required':'required'}))
  repemail = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control','required':'required'}))
  phone = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','required':'required'}))

  class Meta:
    model = University
    fields = '__all__'


class CreateUserForm(UserCreationForm):
  username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
  first_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
  last_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
  email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}))
  password1 = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'type':'password'}))
  password2 = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','type':'password'}))

  class Meta:
    model = User
    fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']

  
class ProfileForm(ModelForm):
  bio = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control'}))
  nationality = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
  national_id = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
  location = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
  birth_date = forms.DateField(widget=forms.DateInput(attrs={'class':'form-control', 'type': 'date'}))
  phone = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))


  class Meta:
    model = Agent
    fields = '__all__'
    exclude = ['user']


class ContactForm(ModelForm):
  name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'required':'required'}))
  email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control','required':'required'}))
  message = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control','required':'required'}))

  class Meta:
    model = Contact
    fields = '__all__'


class SubscribeForm(ModelForm):
  email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control','required':'required'}))

  class Meta:
    model = Subscribe
    fields = ['email']