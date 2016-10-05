from singleServices.models import *
from singleServices.serializers import *
from rest_framework_mongoengine import generics
from rest_framework import views
from rest_framework.response import Response

import pymongo

# MongoDB conection
connection = pymongo.MongoClient("mongodb://localhost")
# DB conection Mongo
db = connection.opendata2

class TenderList(generics.ListAPIView):
	serializer_class = TenderSerializer

	def get_queryset(self):
		queryset = Tender.objects.all()
		for i in self.request.GET:
			if i == 'ocid':
				ocid = self.request.GET.get('ocid')
				queryset =  queryset.filter(ocid=ocid)
			if i == 'status':
				status = self.request.GET.get('status')
				queryset = queryset.filter(status=status)
	 		#Buscar por titulo de tender
			if i == 'title':
				title = self.request.GET.get('title')
				queryset = queryset.filter(title__contains=title)
	 		#Buscar por codigo UNSPSC
			if i == 'items':
				itemsStr = self.request.GET.get('items')
				items = int('0' + itemsStr)
				queryset = queryset.filter(items__id=items)
	 		#Buscar por rengo de valor de tender
	 		#Valor hacia arriba
			if i == 'valueUp':
				value = self.request.GET.get('valueUp')
				queryset = queryset.filter(value__amount__gte=value)
	 		#Valor hacia abajo
			if i == 'valueDown':
				value = self.request.GET.get('valueDown')
				queryset = queryset.filter(value__amount__lte=value)
	 	return queryset


	def get(self, request, *args, **kwargs):
		publisher = {
				"name": "Colombia Compra",
				"uri": "http://datos.colombiacompra.gov.co/"
				}
		publicationPolicy =  "http://www.colombiacompra.gov.co/transparencia/gestion-documental/datos-abiertos"
		response = super(TenderList, self).list(request, args, kwargs)
		response.data['publisher'] = publisher 
		response.data['publicationPolicy'] = publicationPolicy
		response.data['license'] = '?'
		response.data['releases'] = response.data['results']
		del response.data['results']
		return response

class PlanningList(generics.ListAPIView):
	serializer_class = PlanningSerializer

	def get_queryset(self):
		queryset = Planning.objects.all()
		for i in self.request.GET:
			if i == 'ocid':
				ocid = self.request.GET.get('ocid')
				queryset =  queryset.filter(ocid=ocid)
	 	return queryset

	def get(self, request, *args, **kwargs):
		publisher = {
				"name": "Colombia Compra",
				"uri": "http://datos.colombiacompra.gov.co/"
				}
		publicationPolicy =  "http://www.colombiacompra.gov.co/transparencia/gestion-documental/datos-abiertos"
		response = super(TenderList, self).list(request, args, kwargs)
		response.data['publisher'] = publisher 
		response.data['publicationPolicy'] = publicationPolicy
		response.data['license'] = '?'
		response.data['releases'] = response.data['results']
		del response.data['results']
		return response

class AwardsList(generics.ListAPIView):
	serializer_class = AwardsSerializer
	
	def get_queryset(self):
		queryset = Awards.objects.all()
		for i in self.request.GET:
			if i == 'ocid':
				ocid = self.request.GET.get('ocid')
				queryset =  queryset.filter(ocid=ocid)
			if i == 'id':
				id_award = self.request.GET.get('id')
				queryset =  queryset.filter(id=id_award)
	 		#Buscar por codigo UNSPSC
			if i == 'items':
				itemsStr = self.request.GET.get('items')
				items = int('0' + itemsStr)
				queryset = queryset.filter(items__id=items)
	 		#Buscar por rengo de valor de tender
	 		#Valor hacia arriba
			if i == 'valueUp':
				value = self.request.GET.get('valueUp')
				queryset = queryset.filter(value__amount__gte=value)
	 		#Valor hacia abajo
			if i == 'valueDown':
				value = self.request.GET.get('valueDown')
				queryset = queryset.filter(value__amount__lte=value)
	 	return queryset



	def get(self, request, *args, **kwargs):
		publisher = {
				"name": "Colombia Compra",
				"uri": "http://datos.colombiacompra.gov.co/"
				}
		publicationPolicy =  "http://www.colombiacompra.gov.co/transparencia/gestion-documental/datos-abiertos"
		response = super(AwardsList, self).list(request, args, kwargs)
		response.data['publisher'] = publisher 
		response.data['publicationPolicy'] = publicationPolicy
		response.data['license'] = '?'
		response.data['releases'] = response.data['results']
		del response.data['results']
		return response

class ContractsList(generics.ListAPIView):
	serializer_class = ContractsSerializer
	
	def get_queryset(self):
		queryset = Contracts.objects.all()
		for i in self.request.GET:
			if i == 'ocid':
				ocid = self.request.GET.get('ocid')
				queryset =  queryset.filter(ocid=ocid)
			if i == 'id':
				id_contract = self.request.GET.get('id')
				queryset =  queryset.filter(id=id_contract)
	 		#Buscar por codigo UNSPSC
			if i == 'items':
				itemsStr = self.request.GET.get('items')
				items = int('0' + itemsStr)
				queryset = queryset.filter(items__id=items)
	 		#Buscar por rengo de valor de tender
	 		#Valor hacia arriba
			if i == 'valueUp':
				value = self.request.GET.get('valueUp')
				queryset = queryset.filter(value__amount__gte=value)
	 		#Valor hacia abajo
			if i == 'valueDown':
				value = self.request.GET.get('valueDown')
				queryset = queryset.filter(value__amount__lte=value)
	 	return queryset

	def get(self, request, *args, **kwargs):
		publisher = {
				"name": "Colombia Compra",
				"uri": "http://datos.colombiacompra.gov.co/"
				}
		publicationPolicy =  "http://www.colombiacompra.gov.co/transparencia/gestion-documental/datos-abiertos"
		response = super(ContractsList, self).list(request, args, kwargs)
		response.data['publisher'] = publisher 
		response.data['publicationPolicy'] = publicationPolicy
		response.data['license'] = '?'
		response.data['releases'] = response.data['results']
		del response.data['results']
		return response

class EntityList(views.APIView):
	def get(self, request, format=None):
		queryset = db.entity.find()
		for i in self.request.GET:
			if i == 'name':
				name = self.request.GET.get('name')
				queryset = db.entity.find({'_id.name': {'$regex': name, '$options': 'i' } })
			if i == 'nit':
				nit = self.request.GET.get('nit')
				queryset = db.entity.find({'_id.nit': {'$regex': nit} })
		inserted = []
		for doc in queryset:
			inserted.append(doc)
		return Response(inserted)

class StatusList(views.APIView):
	def get(self, request, format=None):
		queryset = db.status.find()
		for i in self.request.GET:
			if i == 'name':
				name = self.request.GET.get('name')
				queryset = db.status.find({'_id.status': {'$regex': name, '$options': 'i' } })
		inserted = []
		for doc in queryset:
			inserted.append(doc)
		return Response(inserted)

class ProcurementTypeList(views.APIView):
	def get(self, request, format=None):
		queryset = db.procurement_type.find()
		for i in self.request.GET:
			if i == 'name':
				name = self.request.GET.get('name')
				queryset = db.procurement_type.find({'_id.name': {'$regex': name, '$options': 'i' } })
		inserted = []
		for doc in queryset:
			inserted.append(doc)
		return Response(inserted)
