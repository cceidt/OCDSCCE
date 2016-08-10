from singleServices.models import *
from singleServices.serializers import *
from rest_framework_mongoengine import generics

class ContractList(generics.ListAPIView):
	serializer_class = ContractsSerializer
	queryset = Contracts.objects.all()
	
class AwardList(generics.ListAPIView):
	serializer_class = AwardsSerializer
	queryset = Awards.objects.all()

class PlanningList(generics.ListAPIView):
	serializer_class = PlanningSerializer
	queryset = Planning.objects.all()