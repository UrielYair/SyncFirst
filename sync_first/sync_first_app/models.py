# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
import datetime

STATUS_OPTIONS = [("pending", "pending"), ("monitored", "monitored"), ("irrelevant", "irrelevant"),
                  ("refuse", "refuse")]


class Person(models.Model):
    # Should by official id (tz)
    identification = models.CharField(max_length=9)
    status = models.CharField(max_length=10, choices=STATUS_OPTIONS, default=STATUS_OPTIONS[0][0])
    last_update = models.DateField(default=datetime.date.today())


class Incident(models.Model):
    main_person = models.ForeignKey(Person, related_name="incidents_reported_by")
    spouse = models.ForeignKey(Person, related_name="incidents_reported_about")
    date = models.DateField(auto_now_add=True)
    # Consider making this a select within given options (valid organizations)
    organization = models.CharField(max_length=30)
    description = models.TextField(max_length=120)
    # Should by official id (tz)
    reporter = models.CharField(max_length=9, null=True, blank=True)
    was_viewed = models.BooleanField(default=False)
