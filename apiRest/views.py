from apiRest.models import *
from apiRest.serializers import *
from rest_framework_mongoengine import generics
from rest_framework import filters
from datetime import datetime

class TendersList(generics.ListAPIView):
    serializer_class = TendersSerializer

    def get_queryset(self):
        queryset = Tenders.objects.all()
        a = ['status','title', 'items', 'value']
        filtro = Tenders.objects.all()
        if 'id_tender' in self.request.GET:
            id_tender = self.request.GET.get('id_tender')
            filtro = Tenders.objects.filter(id_tender=id_tender)
            return filtro
        else:
            for i in a:
                if i in self.request.GET:
                    if i == 'status':
                        status = self.request.GET.get('status')
                        filtro = filtro.filter(status=status)
                    if i == 'title':
                        title = self.request.GET.get('title')
                        filtro = filtro.filter(title__contains=title)
                    if i == 'items':
                        items = self.request.GET.get('items')
                        filtro = filtro.filter(items__id_item=items)
                    if i == 'value':
                        value = self.request.GET.get('value')
                        filtro = filtro.filter(value__amount=value)
                    else:
                        pass
                else:
                    pass
            return filtro

class AwardsList(generics.ListAPIView):
    serializer_class = AwardsSerializer
    def get_queryset(self):
        queryset = Awards.objects.all()
        if 'id_award' in self.request.GET:
            id_award = self.request.GET.get('id_award')
            return Awards.objects.filter(id_award=id_award)
        else:
            return Awards.objects.all()    

class ContractsList(generics.ListAPIView):
    serializer_class = ContractsSerializer
    def get_queryset(self):
        queryset = Contracts.objects.all()
        if 'id_contract' in self.request.GET:
            id_contract = self.request.GET.get('id_contract')
            return Contracts.objects.filter(id_contract=id_contract)
        else:
            return Contracts.objects.all() 


class ReleasesList(generics.ListAPIView):
    serializer_class = ReleasesSerializer

    def get_queryset(self):     
        queryset = Releases.objects.all()
        a = ['name','identifier', 'tag', 'start', 'finish']
        filtro = Releases.objects.all()
        if 'id_release' in self.request.GET:
            id_release = self.request.GET.get('id_release')
            filtro = Releases.objects.filter(id_release=id_release)
            return filtro
        else:
            for i in a:
                if i in self.request.GET:
                    if i == 'name':
                        name = self.request.GET.get('name')
                        filtro = filtro.filter(buyer__identifier__legalName__contains=name)
                    if i == 'identifier':
                        identifier = self.request.GET.get('identifier')
                        filtro = filtro.filter(buyer__identifier__id_ident__contains=identifier)
                    if i == 'tag':
                        tag = self.request.GET.get('tag')
                        filtro = filtro.filter(tag__contains=tag)
                    if i == 'start':
                        start = datetime.strptime((self.request.GET.get('start')),'%Y-%m-%d')
                        filtro = filtro.filter(date__gte=start)
                    if i == 'finish':
                        finish = datetime.strptime((self.request.GET.get('finish')),'%Y-%m-%d')
                        filtro = filtro.filter(date__lte=finish)
                    else:
                        pass
                else:
                    pass
            return filtro

class PlanningList(generics.ListAPIView):
    queryset = Releases.objects.filter(planning__exists=True)
    serializer_class = PlanningSerializer

class PackageList(generics.ListAPIView):
    serializer_class = PackagemetadataSerializer
    def get_queryset(self):
        queryset = Packagemetadata.objects.all()
        if 'num_constancia' in self.request.GET:
            num_constancia = self.request.GET.get('num_constancia')
            return Packagemetadata.objects.filter(num_constancia=num_constancia)
        else:
            return Packagemetadata.objects.all() 