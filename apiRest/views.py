from django.shortcuts import render, get_object_or_404
from apiRest.models import *
from apiRest.serializers import *
from rest_framework_mongoengine import generics
from rest_framework import viewsets
from rest_framework import filters
from django.db.models import Q
from datetime import datetime
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer


class TendersList(generics.ListAPIView):
    queryset = Tenders.objects.all()
    serializer_class = TendersSerializer


class TendersIdList(generics.ListAPIView):
    serializer_class = TendersSerializer

    def get_queryset(self):
        id_tender = self.kwargs['id_tender']
        return Tenders.objects.filter(id_tender=id_tender)

class TendersStatusList(generics.ListAPIView):
    serializer_class = TendersSerializer

    def get_queryset(self):
        status = self.kwargs['status']
        return Tenders.objects.filter(status=status)

class TendersTitleList(generics.ListAPIView):
    serializer_class = TendersSerializer

    def get_queryset(self):
        title = self.kwargs['title']
        return Tenders.objects.filter(title__contains=title)

class TendersItemsList(generics.ListAPIView):
    serializer_class = TendersSerializer

    def get_queryset(self):
        items = self.kwargs['items']
        return Tenders.objects.filter(items__id_item=items)

class TendersValueList(generics.ListAPIView):
    serializer_class = TendersSerializer

    def get_queryset(self):
        value = self.kwargs['value']
        return Tenders.objects.filter(value__amount=value)

class AwardsList(generics.ListAPIView):
    queryset = Awards.objects.all()
    serializer_class = AwardsSerializer

class AwardsIdList(generics.ListAPIView):
    serializer_class = AwardsSerializer

    def get_queryset(self):
        id_award = self.kwargs['id_award']
        return Awards.objects.filter(id_award=id_award)

class ContractsList(generics.ListAPIView):
    queryset = Contracts.objects.all()
    serializer_class = ContractsSerializer

class ContractsIdList(generics.ListAPIView):
    serializer_class = ContractsSerializer

    def get_queryset(self):
        id_contract = self.kwargs['id_contract']
        return Contracts.objects.filter(id_contract=id_contract)

class ReleasesList(generics.ListAPIView):
    queryset = Releases.objects.all()
    serializer_class = ReleasesSerializer

class ReleasesNumConstList(generics.ListAPIView):
    serializer_class = ReleasesSerializer

    def get_queryset(self):
        id_release = self.kwargs['id_release']
        return Releases.objects.filter(id_release=id_release)

class ReleasesBuyerNameList(generics.ListAPIView):
    serializer_class = ReleasesSerializer

    def get_queryset(self):
        name = self.kwargs['name']
        return Releases.objects.filter(buyer__identifier__legalName__contains=name)

class ReleasesBuyerIdenNameList(generics.ListAPIView):
    serializer_class = ReleasesSerializer

    def get_queryset(self):
        identifier = self.kwargs['identifier']
        return Releases.objects.filter(buyer__identifier__id_ident__contains=identifier)

class ReleasesTagNameList(generics.ListAPIView):
    serializer_class = ReleasesSerializer

    def get_queryset(self):
        tag = self.kwargs['tag']
        return Releases.objects.filter(tag__contains=tag)

class ReleasesDateList(generics.ListAPIView):
    serializer_class = ReleasesSerializer

    def get_queryset(self):
        inicio = datetime.strptime((self.kwargs['inicio']),'%Y-%m-%d')
        fin = datetime.strptime((self.kwargs['fin']),'%Y-%m-%d')
        return Releases.objects.filter(date__gte=inicio, date__lte=fin)

# class ReleasesTenderList(generics.ListAPIView):
#     serializer_class = ReleasesSerializer

#     def get_queryset(self):
#         """
#         This view should return a list of all the purchases for
#         the user as determined by the username portion of the URL.
#         """
#         tender = self.kwargs['tender']
#         ref_tender = Tenders.objects.get(id_tender=tender) 
#         print ref_tender.id
#         Prueba = Releases.objects.filter(tender=ref_tender.id)
#         print Prueba
#         return Releases.objects.filter(tender=ref_tender.id)

class PlanningList(generics.ListAPIView):
    queryset = Releases.objects.filter(planning__exists=True)
    serializer_class = PlanningSerializer

class PackageList(generics.ListAPIView):
    queryset = Packagemetadata.objects.all()
    serializer_class = PackagemetadataSerializer

class PackageNumConstList(generics.ListAPIView):
    serializer_class = PackagemetadataSerializer

    def get_queryset(self):
        num_constancia = self.kwargs['num_constancia']
        return Packagemetadata.objects.filter(num_constancia=num_constancia)