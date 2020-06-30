"""total URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, include
from django.urls import reverse
from .views import *


urlpatterns = [
   path('base', base, name='base_url'),
   path('accounts/', include('django.contrib.auth.urls')),
   path('crew_member', crew_member_view, name='crew_member_url'),
   path('add_crew_member', add_crew_member, name='add_crew_member_url'),
   #path('add_crew_member_save', add_crew_member_save, name='add_crew_member_save_url'),
   path('edit_crew_member/<int:crew_member_id>/', edit_crew_member, name='edit_crew_member_url'),
   path('edit_crew_member', edit_crew_member_save, name='edit_save_crew_member_url'),
   path('delete_crew_member/<int:crew_member_id>/', delete_crew_member, name='delete_crew_member_url'),
   path('crew_member/<int:crew_member_id>/', details),

   path('helicopter', helicopter_view, name='helicopter_url'),
   path('add_helicopter', add_helicopter, name='add_helicopter_url'),
   path('edit_helicopter/<int:helicopter_id>/', edit_helicopter, name='edit_helicopter_url'),
   path('edit_helicopter', edit_helicopter_save, name='edit_save_helicopter_url'),
   path('delete_helicopter/<int:helicopter_id>/', delete_helicopter, name='delete_helicopter_url'),
   path('helicopter/<int:helicopter_id>/', details_helicopter),

   path('flight', flight_view, name='flight_url'),
   path('flight1', flight_view1, name='flight1_url'),
   path('add_flight', add_flight, name='add_flight_url'),
   path('edit_flight/<int:flight_id>/', edit_flight, name='edit_flight_url'),
   path('edit_flight', edit_flight_save, name='edit_save_flight_url'),
   path('delete_flight/<int:flight_id>/', delete_flight, name='delete_flight_url'),
   path('flight/<int:flight_id>/', details_flight),

#    path('create_fligh', create_fligh, name='create_fligh_url'),
#    path('create_fligh', details_create_fligh, name='details_create_fligh_url'),
 ]


