from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from total import settings


class flight_information_form(forms.ModelForm):
    class Meta:
        model = flight_information
        fields = ['flight_date', 'cargo_weight', 'number_of_people', 'flight_duration', 'departure', 'arrival', 'status',
                  'id_helicopter', 'id_crew_member_1', 'id_crew_member_2', 'id_crew_member_3']
        widgets = {
            'flight_date': forms.TextInput(attrs={'class' : 'form-control'}),
            'cargo_weight': forms.TextInput(attrs={'class' : 'form-control'}),
            'number_of_people': forms.TextInput(attrs={'class' : 'form-control'}),
            'flight_duration': forms.TextInput(attrs={'class' : 'form-control'}),
            'departure': forms.TextInput(attrs={'class' : 'form-control'}),
            'arrival': forms.TextInput(attrs={'class': 'form-control'}),
            'id_helicopter': forms.TextInput(attrs={'class': 'form-control'}),
            'id_crew_member_1': forms.TextInput(attrs={'class': 'form-control'}),
            'id_crew_member_2': forms.TextInput(attrs={'class': 'form-control'}),
            'id_crew_member_3': forms.TextInput(attrs={'class': 'form-control'}),
            'status': forms.TextInput(attrs={'class': 'form-control'}),
        }


class helicopter_form(forms.ModelForm):
    class Meta:
        model = helicopter
        fields = ['type_helicopter', 'production_date', 'carrying', 'date_of_last_repair', 'time_resource_until_the_next_major_overhaul', 'status']
        widgets = {
            'type_helicopter': forms.TextInput(attrs={'class' : 'form-control'}),
            'production_date': forms.TextInput(attrs={'class' : 'form-control'}),
            'carrying': forms.TextInput(attrs={'class' : 'form-control'}),
            'date_of_last_repair': forms.TextInput(attrs={'class' : 'form-control'}),
            'time_resource_until_the_next_major_overhaul': forms.TextInput(attrs={'class' : 'form-control'}),
            'status': forms.TextInput(attrs={'class': 'form-control'}),
        }
    # type_helicopter = forms.CharField(max_length=50)
    # production_date = forms.DateField()
    # carrying = forms.IntegerField()
    # date_of_last_repair = forms.DateField()
    # time_resource_until_the_next_major_overhaul = forms.TimeField()
    # status = forms.BooleanField()
    #
    # type_helicopter.widget.attrs.update({'class': 'form.control'})
    # production_date.widget.attrs.update({'class': 'form.control'})
    # carrying.widget.attrs.update({'class': 'form.control'})
    # date_of_last_repair.widget.attrs.update({'class': 'form.control'})
    # time_resource_until_the_next_major_overhaul.widget.attrs.update({'class': 'form.control'})
    # status.widget.attrs.update({'class': 'form.control'})


class crew_member_form(forms.ModelForm):
    class Meta:
        model = crew_member
        fields = ['names', 'experience', 'address', 'year_of_birth', 'functions', 'status']
        widgets = {
            'names': forms.TextInput(attrs={'class' : 'form-control'}),
            'experience': forms.TextInput(attrs={'class' : 'form-control'}),
            'address': forms.TextInput(attrs={'class' : 'form-control'}),
            'year_of_birth': forms.TextInput(attrs={'class' : 'form-control'}),
            'functions': forms.TextInput(attrs={'class' : 'form-control'}),
            'status': forms.TextInput(attrs={'class': 'form-control'}),
        }


# class crew_member_form(forms.Form):
#     names = forms.CharField(max_length=50)
#     experience = forms.DateField()
#     address = forms.CharField(max_length=50)
#     year_of_birth = forms.DateField()
#     functions = forms.CharField(max_length=50)
#
#     names.widget.attrs.update({'class': 'form.control'})
#     experience.widget.attrs.update({'class': 'form.control'})
#     address.widget.attrs.update({'class': 'form.control'})
#     year_of_birth.widget.attrs.update({'class': 'form.control'})
#     functions.widget.attrs.update({'class': 'form.control'})


# class flight_form(forms.Form):
#     class Meta:
#         model = crew_member
#         fields = ['id_flight', 'id_helicopter1', 'id_crew_member2', 'id_crew_member3', 'id_crew_member', 'date_of_appointment_of_the_pilot_on_the_helicopter']
#         widgets = {
#             'id_flight': forms.TextInput(attrs={'class' : 'form-control'}),
#             'id_helicopter': forms.TextInput(attrs={'class' : 'form-control'}),
#             'id_crew_member1': forms.TextInput(attrs={'class' : 'form-control'}),
#             'id_crew_member2': forms.TextInput(attrs={'class' : 'form-control'}),
#             'id_crew_member3': forms.TextInput(attrs={'class' : 'form-control'}),
#             'date_of_appointment_of_the_pilot_on_the_helicopter': forms.TextInput(attrs={'class': 'form-control'}),
     #  }
    # id_flight = forms.IntegerField()
    # id_helicopter = forms.IntegerField()
    # id_crew_member = forms.IntegerField()
    # date_of_appointment_of_the_pilot_on_the_helicopter = forms.DateTimeField()
    #
    # id_flight.widget.attrs.update({'class': 'form.control'})
    # id_helicopter.widget.attrs.update({'class': 'form.control'})
    # id_crew_member.widget.attrs.update({'class': 'form.control'})
    # date_of_appointment_of_the_pilot_on_the_helicopter.widget.attrs.update({'class': 'form.control'})


