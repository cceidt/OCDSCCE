from django.conf.urls import patterns, include, url
from singleServices import views
from django.views.generic import RedirectView

urlpatterns = patterns('',
     url(r'^releases/tender/$', views.TenderList.as_view()),
     url(r'^releases/contract/$', views.ContractsList.as_view()),
     url(r'^releases/award/$', views.AwardsList.as_view()),
     url(r'^releases/planning/$', views.PlanningList.as_view()),
     url(r'^releases/entity/$', views.EntityList.as_view()),
     url(r'^releases/status/$', views.StatusList.as_view()),
     url(r'^releases/procurement/$', views.ProcurementTypeList.as_view()),
)