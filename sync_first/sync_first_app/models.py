# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Person(models.Model):
    # Should by official id (tz)
    identification = models.CharField(max_length=9)


class Incident(models.Model):
    main_person = models.ForeignKey(Person)
    spouse = models.ForeignKey(Person)
    date = models.DateField(auto_add_now=True)
    # Consider making this a select within given options (valid organizations)
    organization = models.CharField(max_length=30)
    description = models.TextField(max_length=120)
    # Should by official id (tz)
    reporter = models.CharField(max_length=9, null=True, blank=True)
