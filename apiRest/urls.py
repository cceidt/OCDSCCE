from django.conf.urls import patterns, include, url
from apiRest import views
from rest_framework.routers import DefaultRouter
from rest_framework_mongoengine import routers

#router = routers.MongoDefaultRouter()
#router.register(r'tenders', views.TendersList.as_view(), base_name="tenders")
# router.register(r'release', ReleaseDateViewSet)

urlpatterns = patterns('',
    #url(r'^', include(router.urls)),
     url(r'^tenders/$', views.TendersList.as_view()),
     url(r'^tenders/id/(?P<id_tender>[0-9]+-[0-9]+-[0-9]+)/$', views.TendersIdList.as_view(), name='tenders-id'),
     url(r'^tenders/status/(?P<status>[0-9a-z]+)/$', views.TendersStatusList.as_view(), name='tenders-detail'),
     url(r'^tenders/title/(?P<title>[\w|\W]+)/$', views.TendersTitleList.as_view(), name='tenders-title'),
     url(r'^tenders/items/(?P<items>[\w|\W]+)/$', views.TendersItemsList.as_view(), name='tenders-items'),
     url(r'^tenders/value/(?P<value>[0-9]+)/$', views.TendersValueList.as_view(), name='tenders-items'),                
     url(r'^award/$', views.AwardsList.as_view()),
     url(r'^award/id/(?P<id_award>[0-9]+)/$', views.AwardsIdList.as_view()),
     url(r'^contract/$', views.ContractsList.as_view()),
     url(r'^contract/id/(?P<id_contract>[\w|\W]+)/$', views.ContractsIdList.as_view()),
     url(r'^planning/$', views.PlanningList.as_view()),
     url(r'^releases/$', views.ReleasesList.as_view()),
     url(r'^releases/id/(?P<id_release>[0-9]+-[0-9]+-[0-9]+)/$', views.ReleasesNumConstList.as_view()),
     url(r'^releases/buyer/legalname/(?P<name>[\w|\W]+)/$', views.ReleasesBuyerNameList.as_view()),
     url(r'^releases/buyer/identifier/(?P<identifier>[0-9]+)/$', views.ReleasesBuyerIdenNameList.as_view()),
     url(r'^releases/buyer/identifier/(?P<identifier>[0-9]+-[0-9]+)/$', views.ReleasesBuyerIdenNameList.as_view()),
     url(r'^releases/tag/(?P<tag>[A-Za-z]+)/$', views.ReleasesTagNameList.as_view()), 
     url(r'^releases/date/start/(?P<inicio>[0-9]+-[0-9]+-[0-9]+)/finish/(?P<fin>[0-9]+-[0-9]+-[0-9]+)/$', views.ReleasesDateList.as_view()),    
     url(r'^package/$', views.PackageList.as_view()),
     url(r'^package/constancia/(?P<num_constancia>[0-9]+-[0-9]+-[0-9]+)/$', views.PackageNumConstList.as_view(), name='package-num-constancia'),
     #url(r'^releases/tenderid/(?P<tender>[0-9]+-[0-9]+-[0-9]+)/$', views.ReleasesTenderList.as_view(), name='releases-tenders'),
)