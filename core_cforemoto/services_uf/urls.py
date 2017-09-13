#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.conf.urls import url, include
from django.contrib import admin
from services_uf import views


urlpatterns = [
	url(r'^create/$', views.save_foment_unity),
	url(r'^list/$', views.list_foment_unity),
	url(r'^price/$', views.consult_foment_unity),
]