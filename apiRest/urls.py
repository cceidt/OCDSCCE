from django.conf.urls import patterns, include, url
from apiRest import views
from django.views.generic import RedirectView

urlpatterns = patterns('',
     url(r'^package/$', views.PackageList.as_view()),
     url(r'^package/tender/$', views.TenderList.as_view()),
     url(r'^package/contract/$', views.ContractList.as_view()),
     url(r'^package/award/$', views.AwardList.as_view()),
     url(r'^procurement/$', views.ProcurementTypeList.as_view()),
     url(r'^state/$', views.StateList.as_view()),
     url(r'^entity/$', views.EntityList.as_view()),
     
)