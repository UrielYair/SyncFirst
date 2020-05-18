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
            at_risk.append(person)

    return HttpResponse(serializers.serialize('json', at_risk), content_type="text/json-comment-filtered")


def get_might_be_a_threat(request):
    all_people = Person.objects.all()
    a_threat = []
    for person in all_people:
        if is_a_threat(person):
            a_threat.append(person)

    return HttpResponse(serializers.serialize('json', a_threat), content_type="text/json-comment-filtered")
