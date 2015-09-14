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


class TendersList(viewsets.ModelViewSet):
    queryset = Tenders.objects.all()
    serializer_class = TendersSerializer
    renderer_classes = (JSONRenderer, )

    def get_queryset(self, request, **kwargs):
        return Response(Tenders.objects.all())


class TendersIdList(generics.ListAPIView):
    serializer_class = TendersSerializer

    def get_queryset(self):
        """
        This view should return a list of all the purchases for
        the user as determined by the username portion of the URL.
        """
        id_tender = self.kwargs['id_tender']
        return Tenders.objects.filter(id_tender=id_tender)

class TendersStatusList(generics.ListAPIView):
    serializer_class = TendersSerializer

    def get_queryset(self):
        """
        This view should return a list of all the purchases for
        the user as determined by the username portion of the URL.
        """
        status = self.kwargs['status']
        return Tenders.objects.filter(status=status)

class TendersTitleList(generics.ListAPIView):
    serializer_class = TendersSerializer

    def get_queryset(self):
        """
        This view should return a list of all the purchases for
        the user as determined by the username portion of the URL.
        """
        title = self.kwargs['title']
        return Tenders.objects.filter(title__contains=title)

class TendersItemsList(generics.ListAPIView):
    serializer_class = TendersSerializer

    def get_queryset(self):
        """
        This view should return a list of all the purchases for
        the user as determined by the username portion of the URL.
        """
        items = self.kwargs['items']
        print items
        print Tenders.objects.filter(items__match_=items)
        return Tenders.objects.filter(items__match_=items)

class TendersValueList(generics.ListAPIView):
    serializer_class = TendersSerializer

    def get_queryset(self):
        """
        This view should return a list of all the purchases for
        the user as determined by the username portion of the URL.
        """
        items = self.kwargs['items']
        print items
        return Tenders.objects.filter(value__amount=items)

class TendersDetail(generics.RetrieveAPIView):
    queryset = Tenders.objects.all()
    serializer_class = TendersSerializer
    lookup_field = 'status'

class BuyerList(generics.ListAPIView):
    queryset = Releases.objects.all()
    serializer_class = BuyerSerializer

class BuyerDetail(generics.RetrieveAPIView):
    queryset = Releases.objects.all()
    serializer_class = BuyerSerializer

class AwardsList(generics.ListAPIView):
    queryset = Awards.objects.all()
    serializer_class = AwardsSerializer

class AwardsDetail(generics.RetrieveAPIView):
    queryset = Awards.objects.all()
    serializer_class = AwardsSerializer

class ContractsList(generics.ListAPIView):
    queryset = Contracts.objects.all()
    serializer_class = ContractsSerializer

class ContractsDetail(generics.RetrieveAPIView):
    queryset = Contracts.objects.all()
    serializer_class = ContractsSerializer

class ReleasesList(generics.ListAPIView):
    queryset = Releases.objects.all()
    serializer_class = ReleasesSerializer

class ReleasesNumConstList(generics.ListAPIView):
    serializer_class = ReleasesSerializer

    def get_queryset(self):
        """
        This view should return a list of all the purchases for
        the user as determined by the username portion of the URL.
        """
        id_release = self.kwargs['id_release']
        return Releases.objects.filter(id_release=id_release)

class ReleasesBuyerNameList(generics.ListAPIView):
    serializer_class = ReleasesSerializer

    def get_queryset(self):
        """
        This view should return a list of all the purchases for
        the user as determined by the username portion of the URL.
        """
        name = self.kwargs['name']
        return Releases.objects.filter(buyer__identifier__legalName__contains=name)

class ReleasesBuyerIdenNameList(generics.ListAPIView):
    serializer_class = ReleasesSerializer

    def get_queryset(self):
        """
        This view should return a list of all the purchases for
        the user as determined by the username portion of the URL.
        """
        identifier = self.kwargs['identifier']
        return Releases.objects.filter(buyer__identifier__id_ident__contains=identifier)

class ReleasesTagNameList(generics.ListAPIView):
    serializer_class = ReleasesSerializer

    def get_queryset(self):
        """
        This view should return a list of all the purchases for
        the user as determined by the username portion of the URL.
        """
        tag = self.kwargs['tag']
        print tag
        return Releases.objects.filter(tag__contains=tag)

class ReleasesDateList(generics.ListAPIView):
    serializer_class = ReleasesSerializer

    def get_queryset(self):
        """
        This view should return a list of all the purchases for
        the user as determined by the username portion of the URL.
        """
        inicio = datetime.strptime((self.kwargs['inicio']),'%Y-%m-%d')
        fin = datetime.strptime((self.kwargs['fin']),'%Y-%m-%d')
        print inicio
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