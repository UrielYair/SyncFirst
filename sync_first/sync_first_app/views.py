# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .alerts import get_at_high_risk, get_might_be_a_threat, get_monitored_people, get_events_for_people
from django.http import JsonResponse, HttpResponse
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt
from .models import Person, Incident, STATUS_OPTIONS
import datetime


def get_people_who_might_be_at_risk(request):
    return render(request, 'at_risk.html', {"people": get_at_high_risk()})


def get_people_who_might_be_a_threat(request):
    return render(request, 'a_threat.html', {"people": get_might_be_a_threat()})


def get_events_for_monitored_person(request):
    monitored_people = get_monitored_people()
    events = get_events_for_people(monitored_people)
    # Filter out viewed event. Later we might want to show it in an archive section.
    events = events.filter(was_viewed=False)
    return render(request, 'monitored.html', {"incidents": events})


def get_new_incident_form(request):
    return render(request, "new_incident.html", {})


def search_incidents_by_id(request):
    return render(request, "search_by_id.html", {})


def get_incidents_by_id(request, person_id):
    person = Person.objects.get(identification=person_id)
    incidents = person.incidents_reported_about.all() | person.incidents_reported_by.all()
    # Transform to dict, should be a class method
    incidents = [{'main_id': incident.main_person.identification,
                  'spouse_id': incident.spouse.identification,
                  'date': incident.date, 'organization': incident.organization,
                  'description': incident.description} for incident in incidents]
    return JsonResponse(incidents, safe=False)


@csrf_exempt
def mark_event_as_viewed(request):
    if request.method == 'POST':
        event_id = int(request.POST['event_id'])
        event_obj = Incident.objects.get(id=event_id)
        event_obj.was_viewed = True
        event_obj.save()
        return HttpResponse(status=200)
    else:
        return HttpResponse(status=403)


@csrf_exempt
def change_person_status(request):
    if request.method == 'POST':
        # Get user data and validate it
        person_id = int(request.POST['person_id'])
        status = request.POST['status']
        assert (status, status) in STATUS_OPTIONS

        person_obj = Person.objects.get(id=person_id)
        person_obj.status = status
        person_obj.last_update = datetime.datetime.today()
        person_obj.save()
        return HttpResponse(status=200)
    else:
        return HttpResponse(status=403)
