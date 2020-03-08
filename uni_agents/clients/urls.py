from django.urls import path
from . import views

app_name = 'clients'
urlpatterns = [
  path('', views.index, name='home'),
  path('about/', views.about, name='about'),
  path('contact_us/', views.contact, name='contact'),
  path('agents/register/', views.registerAgent, name='register'),
  path('agents/login/', views.loginAgent, name='login'),
  path('agents/logout/', views.logoutAgent, name='logout'),
  path('agents/profile/', views.agents, name='profile'),
  path('university/event/book', views.uniPortal, name='university'),
  path('events/', views.events, name='events'),
]