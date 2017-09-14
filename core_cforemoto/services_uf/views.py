# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
import datetime
from decimal import Decimal
from openpyxl import load_workbook, Workbook

from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser

from services_uf.models import UnityFoment
from services_uf.serializers import UnityFomentSerializer
from core_cforemoto.settings import STATIC_ROOT as static


@csrf_exempt
def save_foment_unity(request):
	if request.method == 'POST':
		UnityFoment.objects.all().delete()
		file_uf = load_workbook(static+'/historic_uf.xlsx', read_only=True)
		sheet = file_uf.worksheets[0]
		num_fila = 0
		tuple_rows = tuple(sheet.rows)
		historic_uf = []
		i = 0
		for row in tuple_rows:
			if  i > 2:
				historic_uf.append(UnityFoment(date=row[0].value, value=row[1].value))
			i += 1
		UnityFoment.objects.bulk_create(historic_uf)		
		return JsonResponse({'message':'Success'})
	return JsonResponse({'message':'Error'})


def list_foment_unity(request):
	if request.method == 'GET':
		unity_foments = UnityFoment.objects.all()
		serializer = UnityFomentSerializer(unity_foments, many=True)
		return JsonResponse(serializer.data, safe=False)
	return JsonResponse({'message':'Error'})


def consult_foment_unity(request):
	if request.method == 'GET':
		if 'value' not in request.GET or 'date' not in request.GET:
			return JsonResponse({'message':'You must send parameters'})
		try:
			date = datetime.datetime.strptime(request.GET['date'], "%Y%m%d").date()
		except Exception as e:
			return JsonResponse({'message':'Date or date format (yyyymmdd) incorrect '})

		try:
			unity_foments = UnityFoment.objects.get(date=date)
		except Exception as e:
			return JsonResponse({'message':'Error there is no foment unit for the date entered'})

		try:
			value = Decimal(request.GET['value']) 
		except Exception as e:
			return JsonResponse({'message':'You must submit a valid amount'})
		amount =  value/ unity_foments.value
		return JsonResponse({'amount UF':round(amount, 2)}, safe=False)
	return JsonResponse({'message':'Error'})