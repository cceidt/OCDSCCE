from apiRest.models import *
from apiRest.serializers import *
from rest_framework_mongoengine import generics
from rest_framework import filters
from datetime import datetime
import logging

log = logging.getLogger(__name__)

class TendersList(generics.ListAPIView):
    serializer_class = TendersSerializer

    def get_queryset(self):
        queryset = Tenders.objects.all()
        a = ['status','title', 'items', 'value']
        filtro = Tenders.objects.all()
        if 'id_tender' in self.request.GET:
            id_tender = self.request.GET.get('id_tender')
            filtro = Tenders.objects.filter(id_tender=id_tender)
            log.debug("Parametro de busqueda de tender, id_tender: "+ str(id_tender))
            return filtro
        else:
            for i in a:
                if i in self.request.GET:
                    if i == 'status':
                        status = self.request.GET.get('status')
                        filtro = filtro.filter(status=status)
                        log.debug("Parametro de busqueda de tender, status: "+ str(status))
                    if i == 'title':
                        title = self.request.GET.get('title')
                        filtro = filtro.filter(title__contains=title)
                        log.debug("Parametro de busqueda de tender, title: "+ str(title))
                    if i == 'items':
                        items = self.request.GET.get('items')
                        filtro = filtro.filter(items__id_item=items)
                        log.debug("Parametro de busqueda de tender, items - id_item: "+ str(items))
                    if i == 'value':
                        value = self.request.GET.get('value')
                        filtro = filtro.filter(value__amount=value)
                        log.debug("Parametro de busqueda de tender, value: "+ str(value))
                    else:
                        pass
                else:
                    pass
            log.debug("URL busqueda de Tenders: "+ str(self.request.get_full_path()) + " Ip: " + str(self.request.META.get('REMOTE_ADDR')))
            return filtro

class AwardsList(generics.ListAPIView):
    serializer_class = AwardsSerializer
    def get_queryset(self):
        queryset = Awards.objects.all()
        if 'id_award' in self.request.GET:
            id_award = self.request.GET.get('id_award')
            log.debug("Parametro de busqueda de Awards, id_award: "+ str(id_award))
            log.debug("URL busqueda de Awards: "+ str(self.request.get_full_path()) + " Ip: " + str(self.request.META.get('REMOTE_ADDR')))
            return Awards.objects.filter(id_award=id_award)
        else:
            log.debug("URL de busqueda: "+ str(self.request.get_full_path()) + " Ip: " + str(self.request.META.get('REMOTE_ADDR')))
            return Awards.objects.all()    

class ContractsList(generics.ListAPIView):
    serializer_class = ContractsSerializer
    def get_queryset(self):
        queryset = Contracts.objects.all()
        if 'id_contract' in self.request.GET:
            id_contract = self.request.GET.get('id_contract')
            log.debug("Parametro de busqueda de Contracts, id_contract: "+ str(id_contract))
            log.debug("URL busqueda de Contracts: "+ str(self.request.get_full_path()) + " Ip: " + str(self.request.META.get('REMOTE_ADDR')))
            return Contracts.objects.filter(id_contract=id_contract)
        else:
            log.debug("URL de busqueda: "+ str(self.request.get_full_path()) + " Ip: " + str(self.request.META.get('REMOTE_ADDR')))
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
            log.debug("Parametro de busqueda de release, id_release: "+ str(id_release))            
            return filtro
        else:
            for i in a:
                if i in self.request.GET:
                    if i == 'name':
                        name = self.request.GET.get('name')
                        filtro = filtro.filter(buyer__identifier__legalName__contains=name)
                        log.debug("Parametro de busqueda de release, buyer-identifier-legalName: "+ str(name))
                    if i == 'identifier':
                        identifier = self.request.GET.get('identifier')
                        filtro = filtro.filter(buyer__identifier__id_ident__contains=identifier)
                        log.debug("Parametro de busqueda de release, buyer-identifier-id_ident: "+ str(identifier))
                    if i == 'tag':
                        tag = self.request.GET.get('tag')
                        filtro = filtro.filter(tag__contains=tag)
                        log.debug("Parametro de busqueda de release, tag: "+ str(tag))
                    if i == 'start':
                        start = datetime.strptime((self.request.GET.get('start')),'%Y-%m-%d')
                        filtro = filtro.filter(date__gte=start)
                        log.debug("Parametro de busqueda de release, start(fecha inicial): "+ str(start))
                    if i == 'finish':
                        finish = datetime.strptime((self.request.GET.get('finish')),'%Y-%m-%d')
                        filtro = filtro.filter(date__lte=finish)
                        log.debug("Parametro de busqueda de release, finish(fecha final): "+ str(finish))
                    else:
                        pass
                else:
                    pass
            log.debug("URL busqueda de Releases: "+ str(self.request.get_full_path()) + " Ip: " + str(self.request.META.get('REMOTE_ADDR')))
            return filtro

class PlanningList(generics.ListAPIView):
    serializer_class = PlanningSerializer
    def get_queryset(self):
        queryset = Releases.objects.filter(planning__exists=True)
        log.debug("URL busqueda de Planning: "+ str(self.request.get_full_path()) + " Ip: " + str(self.request.META.get('REMOTE_ADDR')))
        return queryset

class PackageList(generics.ListAPIView):
    serializer_class = PackagemetadataSerializer
    def get_queryset(self):
        queryset = Packagemetadata.objects.all()
        if 'num_constancia' in self.request.GET:
            num_constancia = self.request.GET.get('num_constancia')
            log.debug("Busqueda de Package Metadata")
            log.debug("URL de busqueda: "+ str(self.request.get_full_path()) + " Ip: " + str(self.request.META.get('REMOTE_ADDR')))
            return Packagemetadata.objects.filter(num_constancia=num_constancia)
        else:
            log.debug("Busqueda de Package Metadata")
            log.debug("URL de busqueda: "+ str(self.request.get_full_path()) + " Ip: " + str(self.request.META.get('REMOTE_ADDR')))
            return Packagemetadata.objects.all() 