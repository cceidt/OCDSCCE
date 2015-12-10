from django.conf.urls import patterns, include, url
from webApp import views

urlpatterns = patterns('',
     url(r'^results/$', views.PackageList.as_view()),
)