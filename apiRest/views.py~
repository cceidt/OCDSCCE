# -*- encoding: utf-8 -*-
from apiRest.models import *
from apiRest.serializers import *
from rest_framework_mongoengine import generics
from rest_framework import filters
from datetime import datetime
import logging
from rest_framework.exceptions import NotFound
import socket
from django.contrib.auth.decorators import login_required
from rest_framework.settings import api_settings
from rest_framework_csv import renderers as r
from rest_framework import viewsets


log = logging.getLogger(__name__)

class PackageList(generics.ListAPIView):
	serializer_class = PackagemetadataSerializer
	def get_queryset(self):
		queryset = Packagemetadata.objects.all()
		a = ['num_constancia','name','identifier', 'tag', 'start', 'finish','status','title', 'items', 'value', 'id_award', 'id_contract']
		filtro = Packagemetadata.objects.all()
		for i in self.request.GET:
			if i in a:
				if i == 'num_constancia':
					num_constancia = self.request.GET.get('num_constancia')
					filtro =  filtro.filter(num_constancia=num_constancia)
					log.debug("Parametro de busqueda de Packagemetadata, num_constancia: "+ unicode(num_constancia))
					log.debug("URL busqueda de Packagemetadata: "+ unicode(self.request.get_full_path()) + " Ip: " + unicode(self.request.META.get('REMOTE_ADDR')) + " HostName: " + unicode(socket.gethostname()))
				#Buscar por nombe de entidad	
				if i == 'name':
					name = self.request.GET.get('name')
					filtro = filtro.filter(releases__buyer__identifier__legalName__contains=name)
					log.debug("Parametro de busqueda de release, buyer-identifier-legalName: "+ unicode(name))
				#Buscar por nit de entidad
				if i == 'identifier':
					identifier = self.request.GET.get('identifier')
					filtro = filtro.filter(releases__buyer__identifier__id_ident__contains=identifier)
					log.debug("Parametro de busqueda de release, buyer-identifier-id_ident: "+ unicode(identifier))
				#Buscar por tag de release
				if i == 'tag':
					tag = self.request.GET.get('tag')
					filtro = filtro.filter(releases__tag__contains=tag)
					log.debug("Parametro de busqueda de release, tag: "+ unicode(tag))
				#Buscar por fecha inicial
				if i == 'start':
					start = datetime.unicodeptime((self.request.GET.get('start')),'%Y-%m-%d')
					filtro = filtro.filter(releases__date__gte=start)
					log.debug("Parametro de busqueda de release, start(fecha inicial): "+ unicode(start))
				#Buscar por fecha final
				if i == 'finish':
					finish = datetime.unicodeptime((self.request.GET.get('finish')),'%Y-%m-%d')
					filtro = filtro.filter(releases__date__lte=finish)
					log.debug("Parametro de busqueda de release, finish(fecha final): "+ unicode(finish))
				#Buscar por estado de tender
				if i == 'status':
					statust = self.request.GET.get('status')
					filtro = filtro.filter(releases__tender__status=statust)
					log.debug("Parametro de busqueda de tender, status: "+ unicode(statust))
				#Buscar por titulo de tender
				if i == 'title':
					title = self.request.GET.get('title')
					filtro = filtro.filter(releases__tender__title__contains=title)
					log.debug("Parametro de busqueda de tender, title: "+ unicode(title))
				#Buscar por codigo UNSPSC
				if i == 'items':
					items = self.request.GET.get('items')
					filtro = filtro.filter(releases__tender__items__id_item=items)
					log.debug("Parametro de busqueda de tender, items - id_item: "+ unicode(items))
				#Buscar por el valor de tender
				if i == 'value':
					value = self.request.GET.get('value')
					filtro = filtro.filter(releases__tender__value__amount=value)
					log.debug("Parametro de busqueda de tender, value: "+ unicode(value))
				if i == 'id_award':
					id_award = self.request.GET.get('id_award')
					filtro =  filtro.filter(releases__awards__id_award=id_award)
					log.debug("Parametro de busqueda de Awards, id_award: "+ unicode(id_award))
					log.debug("URL busqueda de Awards: "+ unicode(self.request.get_full_path()) + " Ip: " + unicode(self.request.META.get('REMOTE_ADDR')) + " HostName: " + unicode(socket.gethostname()))
				if i == 'id_contract':
					id_contract = self.request.GET.get('id_contract')
					filtro =  filtro.filter(releases__contracts__id_contract=id_contract)
					log.debug("Parametro de busqueda de Awards, id_award: "+ unicode(id_contract))

				#log.warn('-'+ str(i)+'- parameter was not found in Packagemetadata.'+ " Ip: " + unicode(self.request.META.get('REMOTE_ADDR')) + " HostName: " + unicode(socket.gethostname()))
				#raise NotFound('-'+ str(i)+'- parameter was not found in Packagemetadata.')
		log.debug("URL de busqueda Packagemetadata: "+ unicode(self.request.get_full_path()) + " Ip: " + unicode(self.request.META.get('REMOTE_ADDR')) + " HostName: " + unicode(socket.gethostname()))
		return filtro

class MyView(viewsets.ModelViewSet):
	queryset = Packagemetadata.objects.all()
	serializer_class = PackagemetadataSerializer
	renderer_classes = [r.CSVRenderer, ] + api_settings.DEFAULT_RENDERER_CLASSES
