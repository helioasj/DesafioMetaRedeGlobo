from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^contato/$', views.ContatoList.as_view(), name='contato-list'),
    url(r'^contato/(?P<pk>[0-9]+)', views.ContatoDetail.as_view(), name='contato-detail'),

]