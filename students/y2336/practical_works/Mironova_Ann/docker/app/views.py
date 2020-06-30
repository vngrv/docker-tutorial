from django.http import Http404, HttpResponseNotFound
from django.shortcuts import render, redirect
from django.views.generic import View
from django.views.generic.edit import FormView
from .models import *
from .forms import *
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import FormView


def crew_member_view(request):
    context = {}
    context["dataset"] = crew_member.objects.all()
    return render(request, 'crew_member_view.html', context)


def add_crew_member(request):
    context = {}
    form = crew_member_form(request.POST or None)
    if form.is_valid():
        form.save()
    context['form'] = form
    return render(request, "add_crew_member.html", context)
# def add_crew_member_save(request):
#     print('------------+')
#     form = crew_member_form()
#     form.names = request.POST.get("form.names")
#     form.experience = request.POST.get("form.experience")
#     form.address = request.POST.get("form.address")
#     form.year_of_birth = request.POST.get("form.year_of_birth")
#     form.functions = request.POST.get("form.functions")
#     form.save()
#     return redirect('/crew_member')


def details(request, crew_member_id):
    try:
        c = crew_member.objects.get(pk=crew_member_id)
    except crew_member.DoesNotExist:
        raise Http404("Crew member does not exist")
    return render(request, 'crew_member.html', {'crew_member': c})


def edit_crew_member_save(request):
    memberId = request.POST.get("form.id")
    c = crew_member.objects.get(id=memberId)
    c.id = memberId
    c.names = request.POST.get("form.names")
    c.experience = request.POST.get("form.experience")
    c.address = request.POST.get("form.address")
    c.year_of_birth = request.POST.get("form.year_of_birth")
    c.functions = request.POST.get("form.functions")
    c.save()
    return redirect('/crew_member')


def edit_crew_member(request, crew_member_id):
    try:
        c = crew_member.objects.get(id=crew_member_id)
        return render(request, "edit_crew_member.html", {'c': c})
    except crew_member.DoesNotExist:
        return HttpResponseNotFound("<h2>Crew member not found</h2>")


def delete_crew_member(request, crew_member_id):
    try:
        c = crew_member.objects.get(id=crew_member_id)
        c.delete()
        context = {}
        context["dataset"] = crew_member.objects.all()
        return render(request, 'crew_member_view.html', context)
    except crew_member.DoesNotExist:
        return HttpResponseNotFound("<h2>Crew member not found</h2>")


#######################################3
def helicopter_view(request):
    context = {}
    context["dataset"] = helicopter.objects.all()
    return render(request, 'helicopter_view.html', context)


def add_helicopter(request):
    context = {}
    form = helicopter_form(request.POST or None)
    if form.is_valid():
        form.save()
    context['form'] = form
    return render(request, "add_helicopter.html", context)


def details_helicopter(request, helicopter_id):
    try:
        c = helicopter.objects.get(pk=helicopter_id)
    except helicopter.DoesNotExist:
        raise Http404("Helicopter does not exist")
    return render(request, 'helicopter.html', {'helicopter': c})


def edit_helicopter_save(request):
    memberId = request.POST.get("form.id")
    c = helicopter.objects.get(id=memberId)
    c.id = memberId
    c.type_helicopter = request.POST.get("form.type_helicopter")
    c.production_date = request.POST.get("form.production_date")
    c.carrying = request.POST.get("form.carrying")
    c.date_of_last_repair = request.POST.get("form.date_of_last_repair")
    c.time_resource_until_the_next_major_overhaul = request.POST.get("form.time_resource_until_the_next_major_overhaul")
    c.save()
    return redirect('/helicopter')


def edit_helicopter(request, helicopter_id):
    try:
        c = helicopter.objects.get(id=helicopter_id)
        return render(request, "edit_helicopter.html", {'c': c})
    except helicopter.DoesNotExist:
        return HttpResponseNotFound("<h2>Helicopter not found</h2>")


def delete_helicopter(request, helicopter_id):
    try:
        c = helicopter.objects.get(id=helicopter_id)
        c.delete()
        context = {"dataset": helicopter.objects.all()}
        return render(request, 'helicopter_view.html', context)
    except helicopter.DoesNotExist:
        return HttpResponseNotFound("<h2>Helicopter not found</h2>")


#######################################3
def flight_view(request):
    context = {"dataset": flight_information.objects.all()}
    return render(request, 'flight_view.html', context)


def flight_view1(request):
    context = {"dataset": flight_information.objects.all()}
    return render(request, 'details_create_fligh.html', context)


def add_flight(request):
    context = {}
    form = flight_information_form(request.POST or None)
    if form.is_valid():
        form.save()
    context['data_cr'] = crew_member.objects.all()
    context['data_h'] = helicopter.objects.all()
    context['form'] = form
    return render(request, "add_flight.html", context)


def details_flight(request, flight_id):
    try:
        c = flight_information.objects.get(pk=flight_id)
    except flight_information.DoesNotExist:
        raise Http404("Flight does not exist")
    return render(request, 'flight.html', {'flight': c})


def edit_flight_save(request):
    memberId = request.POST.get("form.id")
    c = flight_information.objects.get(id=memberId)
    c.id = memberId
    c.flight_date = request.POST.get("form.flight_date")
    c.cargo_weight = request.POST.get("form.cargo_weight")
    c.number_of_people = request.POST.get("form.number_of_people")
    c.flight_duration = request.POST.get("form.flight_duration")
    c.departure = request.POST.get("form.departure")
    c.arrival = request.POST.get("form.arrival")
    c.save()
    return redirect('/flight')


def edit_flight(request, flight_id):
    try:
        c = flight_information.objects.get(id=flight_id)
        return render(request, "edit_flight.html", {'c': c})
    except flight_information.DoesNotExist:
        return HttpResponseNotFound("<h2>Flight not found</h2>")


def delete_flight(request, flight_id):
    try:
        c = flight_information.objects.get(id=flight_id)
        c.delete()
        context = {"dataset": flight_information.objects.all()}
        return render(request, 'flight_view.html', context)
    except flight_information.DoesNotExist:
        return HttpResponseNotFound("<h2>Flight not found</h2>")


def base(request):
    return render(request, 'base.html')

