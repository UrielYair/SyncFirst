# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Incident, Person

# Register your models here.
admin.site.register(Person)
admin.site.register(Incident)