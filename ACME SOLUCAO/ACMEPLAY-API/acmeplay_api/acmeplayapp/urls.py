from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^acmeplay/$', views.AcmeplayList.as_view(), name='acmeplay-list'),
    url(r'^acmeplay/(?P<pk>[0-9]+)/$', views.AcmeplayList.as_view(), name='acmeplay-detail'),
]