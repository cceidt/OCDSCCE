from apiRest.models import *
from webApp.serializers import *
from rest_framework_mongoengine import generics
from rest_framework import filters
from datetime import datetime
import bson
from itertools import chain

class PackageList(generics.ListAPIView):
    
    def get_serializer_class(self):
        if self.request.method == 'GET' and 'q' in self.request.GET:
            q = request.GET['q']
            if q is not None and q != '':
                tag = self.request.GET.get('tag')
                if 'contract' in tag or 'contractTermination' in tag:
                    return  PackagemetadataContractSerializer
                if 'award' in tag or 'awardCancellation'in tag:
                    return PackagemetadataAwardSerializer
                else:
                    pass
            else:
                pass
        else: pass
        return PackagemetadataSerializer

    def get_queryset(self):     
        queryset = Packagemetadata.objects.all()
        filtro = Packagemetadata.objects.all()
        for i in self.request.GET:
            if 'tag' in i:
            	tag = self.request.GET.get('tag')
                filtro  = filtro.filter(releases__tag__contains=tag)
                for i in self.request.GET:
                    if i == 'num_constancia':
                        num_constancia = self.request.GET.get('num_constancia')
                        print num_constancia
                        filtro = filtro.filter(releases__num_constancia=num_constancia)
                        return filtro
                    if i == 'name':
                        name = self.request.GET.get('name')
                        filtro = filtro.filter(releases__buyer__identifier__legalName__contains=name)
                    if i == 'identifier':
                        identifier = self.request.GET.get('identifier')
                        filtro = filtro.filter(releases__buyer__identifier__id_ident__contains=identifier)
                    if i == 'start':
                        start = datetime.unicodeptime((self.request.GET.get('start')),'%Y-%m-%d')
                        filtro = filtro.filter(releases__date__gte=start)
                    if i == 'finish':
                        finish = datetime.unicodeptime((self.request.GET.get('finish')),'%Y-%m-%d')
                        filtro = filtro.filter(releases__date__lte=finish)
                    else:
                        pass
            else:
            	pass
        return filtro