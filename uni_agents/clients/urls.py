from django.urls import path
from . import views

app_name = 'clients'
urlpatterns = [
  path('', views.index, name='home'),
  path('about/', views.about, name='about'),
  path('contact_us/', views.contact, name='contact'),
  path('agents/register/', views.registerAgent, name='register_agents'),
  path('agents/login/', views.loginAgents, name='login_agents'),
  path('agents/logout', views.loginAgents, name='logout'),
  path('agents/profile/', views.agents, name='profile'),
  path('university/event/book', views.uniPortal, name='university'),
]