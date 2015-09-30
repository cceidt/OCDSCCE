from django.conf.urls import patterns, include, url
from apiRest import views
from django.views.generic import RedirectView

urlpatterns = patterns('',
     url(r'^$', RedirectView.as_view(url='/apirest/releases/')),
     url(r'^tenders/$', views.TendersList.as_view()),
     url(r'^award/$', views.AwardsList.as_view()),
     url(r'^contract/$', views.ContractsList.as_view()),
     url(r'^planning/$', views.PlanningList.as_view()),
     url(r'^releases/$', views.ReleasesList.as_view()),
     url(r'^package/$', views.PackageList.as_view()),
)