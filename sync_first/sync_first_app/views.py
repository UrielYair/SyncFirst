# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .models import Person, Incident
from .alerts import is_a_threat, is_at_risk
from django.http import JsonResponse, HttpResponse
from django.core import serializers


def get_at_high_risk(request):
    all_people = Person.objects.all()
    at_risk = []
    for person in all_people:
        if is_at_risk(person):
            at_risk.append({"person": person.identification,
                            "number_of_events": len(person.incidents_reported_by.all())})

    return JsonResponse(at_risk, safe=False)


def get_might_be_a_threat(request):
    all_people = Person.objects.all()
    a_threat = []
    for person in all_people:
        if is_a_threat(person):
            a_threat.append({"person": person.identification,
                            "number_of_events": len(person.incidents_reported_about.all())})

    return JsonResponse(a_threat, safe=False)
