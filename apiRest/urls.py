from django.conf.urls import patterns, include, url
from apiRest import views
from django.views.generic import RedirectView

urlpatterns = patterns('',
     url(r'^package/$', views.PackageList.as_view()),
)