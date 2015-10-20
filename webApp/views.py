from apiRest.models import *
from webApp.serializers import *
from rest_framework_mongoengine import generics
from rest_framework import filters
from datetime import datetime
import bson
from itertools import chain

class PlaneacionList(generics.ListAPIView):
    serializer_class = PackagemetadataSerializer
    
    def get_queryset(self):     
        queryset = Packagemetadata.objects.all()
        filtro = Packagemetadata.objects.all()
        releases = Releases.objects.all()
        for i in self.request.GET:
            if 'tag' in i:
            	tag = self.request.GET.get('tag')
                releases = releases.filter(tag__contains=tag)
                x = 0
                releases_str = []
                for j in releases:
                    releases_str.append("%s" % releases[x].id)
                    x=x+1
                filtro  = filtro(__raw__={ 'releases': { '$in': releases_str} })
            else:
            	pass
        return filtro

