from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .decorators import unauthenticated_user
from .models import University, Agent
from .forms import UniversityForm, CreateUserForm, ProfileForm, ContactForm, SubscribeForm


# Create your views here.
@unauthenticated_user
def registerAgent(request):
  if request.method == 'POST':
    form = CreateUserForm(request.POST)
    if form.is_valid():
      user = form.save()
      Agent.objects.create(
        user = user
      )
      
      return redirect('clients:login')
    else:
      messages.info(request, 'The two passwords did not match')
  else:
    form = CreateUserForm()

  context = {
    'form': form
  }
  return render(request, 'clients/register-agent.html', context)


@unauthenticated_user
def loginAgent(request):
  if request.method == 'POST':
    username = request.POST.get('username')
    password = request.POST.get('password')

    user = authenticate(request, username=username, password=password)

    if user is not None:
      login(request, user)
      return redirect('clients:profile')
    else:
      messages.info(request, 'Invalid credentials')  

  return render(request, 'clients/login-agent.html')


def logoutAgent(request):
  logout(request)
  return redirect('clients:login')


def index(request):
  context = {
    'hello': 'Hello World'
  }
  return render(request, 'clients/index.html', context)


def about(request):
  if request.method == 'POST':
    form = SubscribeForm(request.POST)
    if form.is_valid():
      form.save()
      form = SubscribeForm()
      messages.success(request, 'Thank you for subscribing with us')
  else:
    form = SubscribeForm()

  context = {
    'form': form
  }

  return render(request, 'clients/about.html', context)


def contact(request):
  if request.method == 'POST':
    form = ContactForm(request.POST)
    if form.is_valid():
      form.save()
      form = ContactForm()
      messages.success(request, 'Your information is saved. We will get back to you with 24hrs. Check your email for feedback')
  else:
    form = ContactForm()

  context = {
    'form': form
  }

  return render(request, 'clients/contact.html', context
  )


def uniPortal(request):

  if request.method == 'POST':
    form = UniversityForm(request.POST)
    if form.is_valid():
      form.save()
      form = UniversityForm()
      messages.info(request, 'Your information has been save successfully. Check your email after 24hours for further guidance')
  else:
    form = UniversityForm()

  context = {
    'form': form
  }

  return render(request, 'clients/university.html', context)


@login_required(login_url='clients:login')
def agents(request):
  agent = request.user.agent

  if request.method == 'POST':
    form = ProfileForm(request.POST, request.FILES,  instance=agent)
    if form.is_valid():
      form.save()
      messages.success(request, 'Your profile was updated successfully')
    else:
      messages.error(request, 'Please correct the error below')
  else:
    form = ProfileForm(instance=agent)
  

  context = {
    'form': form
  }

  return render(request, 'clients/agents.html', context)


def events(request):
  context = {}
  return render(request, 'clients/events.html',context)