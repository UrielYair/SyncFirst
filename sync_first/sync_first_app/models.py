# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Person(models.Model):
    # Should by official id (tz)
    identification = models.CharField(max_length=9)

    def __str__(self):
    	return 'Person('+self.identification + ')'


class Incident(models.Model):
    main_person = models.ForeignKey(Person, related_name="incidents_reported_by")
    spouse = models.ForeignKey(Person, related_name="incidents_reported_about")
    date = models.DateField()
    # Consider making this a select within given options (valid organizations)
    organization = models.CharField(max_length=30)
    description = models.TextField(max_length=120)
    # Should by official id (tz)
    reporter = models.CharField(max_length=9, null=True, blank=True)

    def __str__(self):
        return 'Incident(main_person= '+str(self.main_person) +', spouse= '+ str(self.spouse) +', date= '+ self.date.strftime("%m/%d/%Y) +', organization= '+self.organization+', description= '+ self.description + ', reporter= '+self.reporter + ')'