from django.conf.urls import patterns, include, url
from apiRest import views
from django.views.generic import RedirectView

urlpatterns = patterns('',
     url(r'^releases/$', views.ReleasesList.as_view()),
     url(r'^packagemetadata/$', views.PackageView.as_view()),
     #url(r'^state/$', views.StateList.as_view()),
     #url(r'^entity/$', views.EntityList.as_view()),

)