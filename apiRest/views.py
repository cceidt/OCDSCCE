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
            log.debug("Parametro de busqueda de tender, id_tender: "+ unicode(id_tender))
            return filtro
        else:
            for i in self.request.GET:
                if i in a:
                    if i == 'status':
                        statust = self.request.GET.get('status')
                        filtro = filtro.filter(status=statust)
                        log.debug("Parametro de busqueda de tender, status: "+ unicode(statust))
                    if i == 'title':
                        title = self.request.GET.get('title')
                        filtro = filtro.filter(title__contains=title)
                        log.debug("Parametro de busqueda de tender, title: "+ unicode(title))
                    if i == 'items':
                        items = self.request.GET.get('items')
                        filtro = filtro.filter(items__id_item=items)
                        log.debug("Parametro de busqueda de tender, items - id_item: "+ unicode(items))
                    if i == 'value':
                        value = self.request.GET.get('value')
                        filtro = filtro.filter(value__amount=value)
                        log.debug("Parametro de busqueda de tender, value: "+ unicode(value))
                    else:
                        pass
                else:
                    log.warn('-'+ str(i)+'- parameter was not found in Tenders.'+ " Ip: " + unicode(self.request.META.get('REMOTE_ADDR')) + " HostName: " + unicode(socket.gethostname()))
                    raise NotFound('-'+ str(i)+'- parameter was not found in Tenders.')
            log.debug("URL busqueda de Tenders: "+ unicode(self.request.get_full_path()) + " Ip: " + unicode(self.request.META.get('REMOTE_ADDR')) + " HostName: " + unicode(socket.gethostname()))
            return filtro

class AwardsList(generics.ListAPIView):
    serializer_class = AwardsSerializer
    def get_queryset(self):
        queryset = Awards.objects.all()
        a = ['id_award']
        filtro = Awards.objects.all()
        for i in self.request.GET:
            if i in a:
                id_award = self.request.GET.get('id_award')
                filtro =  filtro.filter(id_award=id_award)
                log.debug("Parametro de busqueda de Awards, id_award: "+ unicode(id_award))
                log.debug("URL busqueda de Awards: "+ unicode(self.request.get_full_path()) + " Ip: " + unicode(self.request.META.get('REMOTE_ADDR')) + " HostName: " + unicode(socket.gethostname()))
            else:
                log.warn('-'+ str(i)+'- parameter was not found in Awards.'+ " Ip: " + unicode(self.request.META.get('REMOTE_ADDR')) + " HostName: " + unicode(socket.gethostname()))
                raise NotFound('-'+ str(i)+'- parameter was not found in Awards.')
        log.debug("URL de busqueda: "+ unicode(self.request.get_full_path()) + " Ip: " + unicode(self.request.META.get('REMOTE_ADDR')) + " HostName: " + unicode(socket.gethostname()))
        return filtro    

class ContractsList(generics.ListAPIView):
    serializer_class = ContractsSerializer
    def get_queryset(self):
        queryset = Contracts.objects.all()
        a = ['id_contract']
        filtro = Contracts.objects.all()
        for i in self.request.GET:
            if i in a:
                id_contract = self.request.GET.get('id_contract')
                filtro =  filtro.filter(id_contract=id_contract)
                log.debug("Parametro de busqueda de Awards, id_award: "+ unicode(id_contract))
                log.debug("URL busqueda de Awards: "+ unicode(self.request.get_full_path()) + " Ip: " + unicode(self.request.META.get('REMOTE_ADDR')) + " HostName: " + unicode(socket.gethostname()))
            else:
                log.warn('-'+ str(i)+'- parameter was not found in Contracts.'+ " Ip: " + unicode(self.request.META.get('REMOTE_ADDR')) + " HostName: " + unicode(socket.gethostname()))
                raise NotFound('-'+ str(i)+'- parameter was not found in Contracts.')
        log.debug("URL de busqueda: "+ unicode(self.request.get_full_path()) + " Ip: " + unicode(self.request.META.get('REMOTE_ADDR')) + " HostName: " + unicode(socket.gethostname()))
        return filtro    


class ReleasesList(generics.ListAPIView):
    serializer_class = ReleasesSerializer

    def get_queryset(self):     
        queryset = Releases.objects.all()
        a = ['name','identifier', 'tag', 'start', 'finish']
        filtro = Releases.objects.all()
        if 'id_release' in self.request.GET:
            id_release = self.request.GET.get('id_release')
            filtro = Releases.objects.filter(id_release=id_release)
            log.debug("Parametro de busqueda de release, id_release: "+ unicode(id_release))            
            return filtro
        else:
            for i in self.request.GET:
                if i in a:
                    if i == 'name':
                        name = self.request.GET.get('name')
                        filtro = filtro.filter(buyer__identifier__legalName__contains=name)
                        log.debug("Parametro de busqueda de release, buyer-identifier-legalName: "+ unicode(name))
                    if i == 'identifier':
                        identifier = self.request.GET.get('identifier')
                        filtro = filtro.filter(buyer__identifier__id_ident__contains=identifier)
                        log.debug("Parametro de busqueda de release, buyer-identifier-id_ident: "+ unicode(identifier))
                    if i == 'tag':
                        tag = self.request.GET.get('tag')
                        filtro = filtro.filter(tag__contains=tag)
                        log.debug("Parametro de busqueda de release, tag: "+ unicode(tag))
                    if i == 'start':
                        start = datetime.unicodeptime((self.request.GET.get('start')),'%Y-%m-%d')
                        filtro = filtro.filter(date__gte=start)
                        log.debug("Parametro de busqueda de release, start(fecha inicial): "+ unicode(start))
                    if i == 'finish':
                        finish = datetime.unicodeptime((self.request.GET.get('finish')),'%Y-%m-%d')
                        filtro = filtro.filter(date__lte=finish)
                        log.debug("Parametro de busqueda de release, finish(fecha final): "+ unicode(finish))
                    else:
                        pass
                else:
                    log.warn('-'+ str(i)+'- parameter was not found in Releases.'+ " Ip: " + unicode(self.request.META.get('REMOTE_ADDR')) + " HostName: " + unicode(socket.gethostname()))
                    raise NotFound('-'+ str(i)+'- parameter was not found in Releases.')
            log.debug("URL busqueda de Releases: "+ unicode(self.request.get_full_path()) + " Ip: " + unicode(self.request.META.get('REMOTE_ADDR')) + " HostName: " + unicode(socket.gethostname()))
            return filtro

class PlanningList(generics.ListAPIView):
    serializer_class = PlanningSerializer
    def get_queryset(self):
        queryset = Releases.objects.filter(planning__exists=True)
        for i in self.request.GET:
            if self.request.GET is None:
                log.debug("URL busqueda de Planning: "+ unicode(self.request.get_full_path()) + " Ip: " + unicode(self.request.META.get('REMOTE_ADDR')) + " HostName: " + unicode(socket.gethostname()))
            else:
                log.warn('-'+ str(i)+'- parameter was not found in Packagemetadata.'+ " Ip: " + unicode(self.request.META.get('REMOTE_ADDR')) + " HostName: " + unicode(socket.gethostname()))
                raise NotFound('-'+ str(i)+'- parameter was not found in Packagemetadata.')
        return queryset

class PackageList(generics.ListAPIView):
    serializer_class = PackagemetadataSerializer
    def get_queryset(self):
        queryset = Packagemetadata.objects.all()
        a = ['num_constancia']
        filtro = Packagemetadata.objects.all()
        for i in self.request.GET:
            if i in a:
                num_constancia = self.request.GET.get('num_constancia')
                filtro =  filtro.filter(num_constancia=num_constancia)
                log.debug("Parametro de busqueda de Packagemetadata, num_constancia: "+ unicode(num_constancia))
                log.debug("URL busqueda de Packagemetadata: "+ unicode(self.request.get_full_path()) + " Ip: " + unicode(self.request.META.get('REMOTE_ADDR')) + " HostName: " + unicode(socket.gethostname()))
            else:
                log.warn('-'+ str(i)+'- parameter was not found in Packagemetadata.'+ " Ip: " + unicode(self.request.META.get('REMOTE_ADDR')) + " HostName: " + unicode(socket.gethostname()))
                raise NotFound('-'+ str(i)+'- parameter was not found in Packagemetadata.')
        log.debug("URL de busqueda Packagemetadata: "+ unicode(self.request.get_full_path()) + " Ip: " + unicode(self.request.META.get('REMOTE_ADDR')) + " HostName: " + unicode(socket.gethostname()))
        return filtro