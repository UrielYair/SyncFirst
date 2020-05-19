# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .alerts import get_at_high_risk, get_might_be_a_threat, get_monitored_people, get_events_for_people
from django.http import JsonResponse, HttpResponse
from django.core import serializers


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
