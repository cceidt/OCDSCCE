from django.conf.urls import patterns, include, url
from apiRest import views
from singleServices.views import AwardList, ContractList, PlanningList
from django.views.generic import RedirectView

urlpatterns = patterns('',
     url(r'^package/$', views.PackageList.as_view()),
     url(r'^package/tender/$', views.TenderList.as_view()),
     url(r'^package/contract/$', ContractList.as_view()),
     url(r'^package/award/$', AwardList.as_view()),
     url(r'^package/planning/$', PlanningList.as_view()),
     url(r'^procurement/$', views.ProcurementTypeList.as_view()),
     url(r'^state/$', views.StateList.as_view()),
     url(r'^entity/$', views.EntityList.as_view()),
     
)