# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Incident(models.Model):
    main_person = models.CharField(max_length=9)
    spouse = models.CharField(max_length=9)
    date = models.DateField()
    organization = models.CharField(max_length=30)
    description = models.CharField(max_length=120)
    reporter = models.CharField(max_length=9, null=True, blank=True)
