from django.shortcuts import render

# Create your views here.
def registerAgent(request):
  context = {

  }
  return render(request, 'clients/register-agent.html', context)


def loginAgents(request):
  context = {

  }
  return render(request, 'clients/login-agent.html', context)


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
  context = {
    'title': 'University Portal'
  }

  return render(request, 'clients/university.html', context)


def agents(request):
  context = {
    'title': 'Agents Portal'
  }

  return render(request, 'clients/agents.html', context)