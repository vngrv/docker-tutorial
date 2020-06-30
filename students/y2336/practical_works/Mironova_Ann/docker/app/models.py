from django.db import models
from django.shortcuts import reverse
from django.contrib.auth import get_user_model
User = get_user_model()


class helicopter(models.Model):
    type_helicopter = models.CharField(max_length=50)
    production_date = models.DateField()
    carrying = models.IntegerField()
    date_of_last_repair = models.DateField()
    time_resource_until_the_next_major_overhaul = models.TimeField()
    status = models.BooleanField(default=False)


class flight_information(models.Model):
    flight_date = models.DateField()
    cargo_weight = models.IntegerField()
    number_of_people = models.IntegerField()
    flight_duration = models.TimeField()
    departure = models.CharField(max_length=50)
    arrival = models.CharField(max_length=50)
    status = models.BooleanField(default=False)
    id_helicopter = models.IntegerField(null=True, blank=True)
    id_crew_member_1 = models.IntegerField(null=True, blank=True)
    id_crew_member_2 = models.IntegerField(null=True, blank=True)
    id_crew_member_3 = models.IntegerField(null=True, blank=True)


class crew_member(models.Model):
    names = models.CharField(max_length=50)
    experience = models.DateField()
    address = models.CharField(max_length=50)
    year_of_birth = models.DateField()
    functions = models.CharField(max_length=50)
    status = models.BooleanField(default=False)


class flight(models.Model):
    date_of_appointment_of_the_pilot_on_the_helicopter = models.DateTimeField(auto_now_add=True)
#     id_flight = models.ForeignKey(flight_information, on_delete=models.CASCADE, default='')
#     id_helicopter = models.ForeignKey(helicopter, on_delete=models.CASCADE, default='')
#     #id_crew_member = models.ForeignKey(crew_member, on_delete=models.CASCADE, default=None)
    # id_flight = models.ForeignKey(flight_information, on_delete=models.CASCADE)
    # id_helicopter = models.ForeignKey(helicopter, on_delete=models.CASCADE)
    # date_of_appointment_of_the_pilot_on_the_helicopter = models.DateTimeField(auto_now_add=True)


class helicopter_crew_identification(models.Model):
    date_of_appointment_of_crew_on_the_helicopter = models.DateField()
    # id_crew_member = models.ForeignKey(crew_member, on_delete=models.CASCADE)
    # id_helicopter = models.ForeignKey(helicopter, on_delete=models.CASCADE)



def __str__(self):
        return self.title

