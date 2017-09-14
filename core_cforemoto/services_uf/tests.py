# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase

# Create your tests here.
import json
import datetime

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from services_uf.models import UnityFoment

class UnityFomentPriceTests(APITestCase):
    def test_price_unity_foment(self):
		date = datetime.datetime.strptime('20170902', "%Y%m%d").date()
		UnityFoment(date=date, value=26607.53).save()
		url = reverse('uf_price')
		data = {'value': '100000', 'date':'20170902'}
		response = self.client.get(url, data)
		self.assertEqual(json.loads(response.content), {'amount UF': 3.76})


class UnityFomentCreateTests(APITestCase):
	def test_create_unity_foment(self):
		url = reverse('uf_create')
		response = self.client.post(url)
		self.assertEqual(json.loads(response.content), {"message": "Success"})


class UnityFomentListTests(APITestCase):
	def test_list_unity_foment(self):
		url = reverse('uf_list')
		response = self.client.get(url)
		self.assertEqual(response.status_code, 200)


if __name__ == '__main__':
	test_create_unity_foment.main()

if __name__ == '__main__':
    test_price_unity_foment.main()

if __name__ == '__main__':
	test_list_unity_foment.main()