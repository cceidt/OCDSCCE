from apiRest.models import *
from webApp.serializers import *
from rest_framework_mongoengine import generics
from rest_framework import filters
from datetime import datetime
import bson
from itertools import chain

class PackageList(generics.ListAPIView):

	def get_serializer_class(self):
		if self.request.method == 'GET':
			if self.request.GET is not None and self.request.GET != '':
				if 'tag' in self.request.GET:
					tag = self.request.GET.get('tag')
					if 'contract' in tag or 'contractTermination' in tag:
						return  PackagemetadataContractSerializer
					if 'award' in tag or 'awardCancellation'in tag:
						return PackagemetadataAwardSerializer
					else:
						return PackagemetadataSerializer
			return PackagemetadataSerializer

	def get_queryset(self):     
		queryset = Packagemetadata.objects.all()
		filtro = Packagemetadata.objects.all()
		for i in self.request.GET:
			if 'tag' in i:
				tag = self.request.GET.get('tag')
				filtro  = filtro.filter(releases__tag__contains=tag)
                for i in self.request.GET:
                	  #Buscar por estado del proceso de contratacion
					if i == 'status':
						status = self.request.GET.get('status')
						if tag == 'tender' or tag == 'planning':
							#Buscar por estado de tender
							filtro = filtro.filter(releases__tender__status=status)
						if tag == 'award' or tag == 'awardCancellation':
							#Buscar por estado de awards
							filtro = filtro.filter(releases__awards__status=status)
						if tag == 'contract' or tag == 'contractTermination':
							#Buscar por estado de contracts
							filtro = filtro.filter(releases__contracts__status=status)
					#Falta el metodo para la busqueda por modalidad de contratacion

					#Buscar por numero de constancia
					if i == 'num_constancia':
						num_constancia = self.request.GET.get('num_constancia')
						filtro = filtro.filter(num_constancia=num_constancia)
						return filtro
					#Buscar por categoria del contrato, por codigo UNSPSC
					if i == 'items':
						items = self.request.GET.get('items')
						filtro = filtro.filter(releases__tender__items__id_item=items)
					#Buscar por fecha
					#Fecha inicio
					if i == 'start':
						start = self.request.GET.get('start')
						filtro = filtro.filter(releases__date__gte=start)
                    #Fecha fin
					if i == 'finish':
						finish = self.request.GET.get('finish')
						filtro = filtro.filter(releases__date__lte=finish)
					#Buscar por departamento de ejecucion
					if i == 'region':
						region = self.request.GET.get('region')
						filtro = filtro.filter(releases__buyer__address__region=region)
					#Buscar por municipio de ejecucion
					if i == 'locality':
						locality = self.request.GET.get('locality')
						filtro = filtro.filter(releases__buyer__address__region=locality)
					#Buscar por nombre de entidad compradora
					if i == 'name':
						name = self.request.GET.get('name')
						filtro = filtro.filter(releases__buyer__identifier__legalName__contains=name)
					#Buscar por Nit de la entidad compradora
					if i == 'identifier':
						identifier = self.request.GET.get('identifier')
						filtro = filtro.filter(releases__buyer__identifier__id__contains=identifier)
					else:
						pass
		return filtro
