# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Person(models.Model):
    identification = models.CharField(max_length=9)


class Incident(models.Model):
    main_person = models.ForeignKey(Person)
    spouse = models.ForeignKey(Person)
    date = models.DateField()
    organization = models.CharField(max_length=30)
    description = models.CharField(max_length=120)
    reporter = models.CharField(max_length=9, null=True, blank=True)
