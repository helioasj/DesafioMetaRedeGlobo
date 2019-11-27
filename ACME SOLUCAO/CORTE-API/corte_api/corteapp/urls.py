from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^videos/$', views.VideosList.as_view(), name='videos-list'),
    url(r'^videos/(?P<pk>[0-9]+)/$', views.VideosDetail.as_view(), name='videos-detail'),
]