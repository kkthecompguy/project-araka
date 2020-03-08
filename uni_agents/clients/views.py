from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import University, Agent
from .forms import UniversityForm, CreateUserForm, ProfileForm


# Create your views here.
def registerAgent(request):
  form = CreateUserForm()

  if request.method == 'POST':
    form = CreateUserForm(request.POST)
    if form.is_valid():
      user = form.save()
      Agent.objects.create(
        user = user
      )
      
      return redirect('clients:login_agents')
    else:
      messages.info(request, 'The two passwords did not match')

  context = {
    'form': form
  }
  return render(request, 'clients/register-agent.html', context)


def loginAgents(request):
  if request.method == 'POST':
    username = request.POST.get('username')
    password = request.POST.get('password')

    user = authenticate(request, username=username, password=password)

    if user is not None:
      login(request, user)
      return redirect('clients:profile')
    else:
      messages.info(request, 'Invalid credentials')  

  context = {

  }
  return render(request, 'clients/login-agent.html', context)


def logoutAgent(request):
  logout(request)
  return redirect('clients:login')


def index(request):
  context = {
    'hello': 'Hello World'
  }
  return render(request, 'clients/index.html', context)


def about(request):
  context = {
    'title': 'About Page'
  }

  return render(request, 'clients/about.html', context)


def contact(request):
  context = {
    'title': 'Hello world'
  }

  return render(request, 'clients/contact.html', context
  )


def uniPortal(request):

  if request.method == 'POST':
    form = UniversityForm(request.POST)
    if form.is_valid():
      form.save()
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