# -*- encoding: utf-8 -*-
import os
from apiRest.models import *
from apiRest.serializers import *
from rest_framework_mongoengine import generics
from rest_framework import filters, views, status
from datetime import datetime
from rest_framework.exceptions import NotFound
import socket
from django.db.models import Count
import pymongo
from bson.code import Code
from rest_framework.response import Response
from django.core import serializers
from bson.json_util import dumps
from bson import json_util 
from rest_framework_csv import renderers as r
import re
from rest_framework.renderers import JSONRenderer


class ReleasesList(generics.ListAPIView):
	serializer_class = ReleasesSerializer
	renderer_classes = (JSONRenderer, )

	def get_queryset(self):
		queryset = Releases.objects.all()
		for i in self.request.GET:
			if i == 'ocid':
				ocid = self.request.GET.get('ocid')
				queryset =  queryset.filter(ocid=ocid)
			if i == 'num_constancia':
				num_constancia = 'ocds-k50g02-' + self.request.GET.get('num_constancia')
				queryset =  queryset.filter(ocid=num_constancia)
	 		#Buscar por modealidad de contratacion
			if i == 'procurement_type':
				procurement_type = self.request.GET.get('procurement_type')
				queryset =  queryset.filter(procurement_type=procurement_type)
	 		#Buscar por nombe de entidad	
			if i == 'name':
				name = self.request.GET.get('name')
				queryset = queryset.filter(buyer__identifier__legalName__contains=name)
	 		#Buscar por nit de entidad
			if i == 'identifier':
				identifier = self.request.GET.get('identifier')
				queryset = queryset.filter(buyer__identifier__id__contains=identifier)
	 		#Buscar por tag de release
			if i == 'tag':
				tag = self.request.GET.get('tag')
				queryset = queryset.filter(tag__contains=tag)
	 		#Buscar por fecha inicial
			if i == 'start':
				start = self.request.GET.get('start')
				queryset = queryset.filter(date__gte=start)
	 		#Buscar por fecha final
			if i == 'finish':
				finish = self.request.GET.get('finish')
				queryset = queryset.filter(date__lte=finish)
	 		#Buscar por estado de tender
			if i == 'status':
				status = self.request.GET.get('status')
				queryset = queryset.filter(tender__status=status)
	 		#Buscar por titulo de tender
			if i == 'title':
				title = self.request.GET.get('title')
				queryset = queryset.filter(tender__title__contains=title)
	 		#Buscar por codigo UNSPSC
			if i == 'items':
				itemsStr = self.request.GET.get('items')
				items = int('0' + itemsStr)
				queryset = queryset.filter(tender__items__id=items)
	 		#Buscar por rengo de valor de tender
	 		#Valor hacia arriba
			if i == 'valueUp':
				value = self.request.GET.get('valueUp')
				queryset = queryset.filter(tender__value__amount__gte=value)
	 		#Valor hacia abajo
			if i == 'valueDown':
				value = self.request.GET.get('valueDown')
				queryset = queryset.filter(tender__value__amount__lte=value)
			if i == 'id_award':
				id_award = self.request.GET.get('id_award')
				queryset =  queryset.filter(awards__id=id_award)
			if i == 'id_contract':
				id_contract = self.request.GET.get('id_contract')
				queryset =  queryset.filter(contracts__id=id_contract)
	 	return queryset

	def get(self, request, *args, **kwargs):
		publisher = {
				"name": "Colombia Compra",
				"uri": "https://www.colombiacompra.gov.co/"
				}
		publicationPolicy =  "http://www.colombiacompra.gov.co/transparencia/gestion-documental/datos-abiertos"
		response = super(ReleasesList, self).list(request, args, kwargs)
		links = {
				"count": response.data['count'],
				"prev": response.data['previous'],
				"next": response.data['next']

		}
		response.data['links'] = links 
		response.data['publisher'] = publisher 
		response.data['publicationPolicy'] = publicationPolicy
		response.data['license'] = 'https://creativecommons.org/licenses/by-sa/2.5/co/legalcode'
		response.data['releases'] = response.data['results']
		response.data['releases'][0]['date'] = response.data['releases'][0]['publishedDate']
		del response.data['results']
		del response.data['count']
		del response.data['previous']
		del response.data['next']
		del response.data['releases'][0]['publishedDate']
		return response

class PackageView(generics.ListAPIView):
	serializer_class = ReleasesSerializer
	renderer_classes = (JSONRenderer, )

	def get_queryset(self):
		if 'ocid' in self.request.GET:
			return Releases.objects.filter(ocid=self.request.GET.get('ocid'))
		else:
			return Response({"Response": "Por favor ingrese el parámetro ocid / Please enter ocid parameter"}, status=status.HTTP_400_BAD_REQUEST)

	def get(self, request, *args, **kwargs):
		publisher = {
				"name": "Colombia Compra",
				"uri": "https://www.colombiacompra.gov.co/"
				}
		response = super(PackageView, self).list(request, args, kwargs)
		response.data['publishedDate'] = response.data['results'][0]['publishedDate']
		response.data['uri'] = response.data['results'][0]['uri']
		response.data['publisher'] = publisher 
		response.data['publicationPolicy'] = 'http://www.colombiacompra.gov.co/transparencia/gestion-documental/datos-abiertos'
		response.data['license'] = 'https://creativecommons.org/licenses/by-sa/2.5/co/legalcode'
		response.data['releases'] = response.data['results'][0]
		del response.data['results']
		del response.data['count']
		del response.data['next']
		del response.data['previous']
		return response