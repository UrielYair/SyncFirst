# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import Incident, Person

from django.shortcuts import render
from .alerts import get_at_high_risk, get_might_be_a_threat
from django.http import JsonResponse, HttpResponse, Http404
from django.core import serializers


# Create your views here.
def show_new_incident_page(request):
    return render(request, 'new_incident.html')

def all_incidents(request):
    context = {
        "incidents" : Incident.objects.all()
    }
    return render(request, "all_incidents.html", context)

def get_incident_by_id(request, incident_id):    
    try:
        context = {
            "incident": Incident.objects.get(pk=incident_id)
        }
    except Incident.DoesNotExist:
        raise Http404("Incident not found.")

    return render(request, "incident.html", context)


def search_person(request):
    return render(request, 'search.html')

def get_incidents_by_person_id(request, person_id_number):
    
    incidents_lists = []
    incidents = Incident.objects.all()
    
    for incident in incidents:
        if incident.main_person == person_id_number or incident.spouse == person_id_number:
            incidents_lists.append(incident)
    
    context={
        'person_id': person_id_number,
        'incidents': incidents_lists
    }
    
    return render(request, 'all_incidents_by_id.html', context)

def store_new_incident(request, incident_to_save):
    inc = Incident({
        main_person: Person(incident_to_save.main_person).save(),
        spouse: Person(incident_to_save.spouse).save(),
        date: datetime.date.today(),
        organization: incident_to_save.organization,
        description: incident_to_save.description,
        reporter: incident_to_save.reporter
    })    
    inc.save()
    

def get_people_who_might_be_at_risk(request):
    return render(request, 'at_risk.html', {"people": get_at_high_risk()})


def get_people_who_might_be_a_threat(request):
    return render(request, 'a_threat.html', {"people": get_might_be_a_threat()})

