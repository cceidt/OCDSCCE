from singleServices.models import *
from singleServices.serializers import *
from rest_framework_mongoengine import generics
from rest_framework import views
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
import pymongo

# MongoDB conection
connection = pymongo.MongoClient("mongodb://cceproocds020.compute-a18530.oraclecloud.internal:5017")
# DB conection Mongo
db = connection.opendata

class TenderList(generics.ListAPIView):
	serializer_class = TenderSerializer
	renderer_classes = (JSONRenderer, )

	def get_queryset(self):
		queryset = Tender.objects.all()
		for i in self.request.GET:
			if i == 'ocid':
				ocid = self.request.GET.get('ocid')
				queryset =  queryset.filter(ocid=ocid)
			if i == 'num_constancia':
				num_constancia = 'ocds-k50g02-' + self.request.GET.get('num_constancia')
				queryset =  queryset.filter(ocid=num_constancia)
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
				"uri": "https://www.colombiacompra.gov.co/"
				}
		publicationPolicy =  "http://www.colombiacompra.gov.co/transparencia/gestion-documental/datos-abiertos"
		response = super(TenderList, self).list(request, args, kwargs)
		links = {
				"count": response.data['count'],
				"prev": response.data['previous'],
				"next": response.data['next']

		}
		response.data['links'] = links 
		response.data['publisher'] = publisher 
		response.data['publicationPolicy'] = publicationPolicy
		response.data['license'] = 'https://creativecommons.org/licenses/by-sa/2.5/co/legalcode'
		response.data['tenders'] = response.data['results']
		del response.data['results']
		del response.data['count']
		del response.data['previous']
		del response.data['next']
		return response

class PlanningList(generics.ListAPIView):
	serializer_class = PlanningSerializer
	renderer_classes = (JSONRenderer, )

	def get_queryset(self):
		queryset = Planning.objects.all()
		for i in self.request.GET:
			if i == 'ocid':
				ocid = self.request.GET.get('ocid')
				queryset =  queryset.filter(ocid=ocid)
			if i == 'num_constancia':
				num_constancia = 'ocds-k50g02-' + self.request.GET.get('num_constancia')
				queryset =  queryset.filter(ocid=num_constancia)
	 	return queryset

	def get(self, request, *args, **kwargs):
		publisher = {
				"name": "Colombia Compra",
				"uri": "https://www.colombiacompra.gov.co/"
				}
		publicationPolicy =  "http://www.colombiacompra.gov.co/transparencia/gestion-documental/datos-abiertos"
		response = super(PlanningList, self).list(request, args, kwargs)
		links = {
				"count": response.data['count'],
				"prev": response.data['previous'],
				"next": response.data['next']

		}
		response.data['links'] = links 
		response.data['publisher'] = publisher 
		response.data['publicationPolicy'] = publicationPolicy
		response.data['license'] = 'https://creativecommons.org/licenses/by-sa/2.5/co/legalcode'
		response.data['plannings'] = response.data['results']
		del response.data['results']
		del response.data['count']
		del response.data['previous']
		del response.data['next']
		return response

class AwardsList(generics.ListAPIView):
	serializer_class = AwardsSerializer
	renderer_classes = (JSONRenderer, )

	def get_queryset(self):
		queryset = Awards.objects.all()
		for i in self.request.GET:
			if i == 'ocid':
				ocid = self.request.GET.get('ocid')
				queryset =  queryset.filter(ocid=ocid)
			if i == 'num_constancia':
				num_constancia = 'ocds-k50g02-' + self.request.GET.get('num_constancia')
				queryset =  queryset.filter(ocid=num_constancia)
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
				"uri": "https://www.colombiacompra.gov.co/"
				}
		publicationPolicy =  "http://www.colombiacompra.gov.co/transparencia/gestion-documental/datos-abiertos"
		response = super(AwardsList, self).list(request, args, kwargs)
		links = {
				"count": response.data['count'],
				"prev": response.data['previous'],
				"next": response.data['next']

		}
		response.data['links'] = links 
		response.data['publisher'] = publisher 
		response.data['publicationPolicy'] = publicationPolicy
		response.data['license'] = 'https://creativecommons.org/licenses/by-sa/2.5/co/legalcode'
		response.data['awards'] = response.data['results']
		del response.data['results']
		del response.data['count']
		del response.data['previous']
		del response.data['next']
		return response

class ContractsList(generics.ListAPIView):
	serializer_class = ContractsSerializer
	renderer_classes = (JSONRenderer, )
	
	def get_queryset(self):
		queryset = Contracts.objects.all()
		for i in self.request.GET:
			if i == 'ocid':
				ocid = self.request.GET.get('ocid')
				queryset =  queryset.filter(ocid=ocid)
			if i == 'num_constancia':
				num_constancia = 'ocds-k50g02-' + self.request.GET.get('num_constancia')
				queryset =  queryset.filter(ocid=num_constancia)
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
				"uri": "https://www.colombiacompra.gov.co/"
				}
		publicationPolicy =  "http://www.colombiacompra.gov.co/transparencia/gestion-documental/datos-abiertos"
		response = super(ContractsList, self).list(request, args, kwargs)
		links = {
				"count": response.data['count'],
				"prev": response.data['previous'],
				"next": response.data['next']

		}
		response.data['links'] = links 
		response.data['publisher'] = publisher 
		response.data['publicationPolicy'] = publicationPolicy
		response.data['license'] = 'https://creativecommons.org/licenses/by-sa/2.5/co/legalcode'
		response.data['contracts'] = response.data['results']
		del response.data['results']
		del response.data['count']
		del response.data['previous']
		del response.data['next']
		return response

class EntityList(views.APIView):
	renderer_classes = (JSONRenderer, )

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
			print doc
			inserted.append(doc)
		return Response(inserted)

class StatusList(views.APIView):
	renderer_classes = (JSONRenderer, )

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
	renderer_classes = (JSONRenderer, )
	
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
