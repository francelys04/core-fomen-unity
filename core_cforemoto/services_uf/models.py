# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class UnityFoment(models.Model):
    date = models.DateField()
    value = models.DecimalField(max_digits=19, decimal_places=2)

    class Meta:
        ordering = ('date',)