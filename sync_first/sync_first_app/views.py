# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .alerts import get_at_high_risk, get_might_be_a_threat
from django.http import JsonResponse, HttpResponse
from django.core import serializers


def get_people_who_might_be_at_risk(request):
    return render(request, 'at_risk.html', {"people": get_at_high_risk()})


def get_people_who_might_be_a_threat(request):
    return render(request, 'templates/at_risk.html', {"people": get_at_high_risk()})
