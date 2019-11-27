from django.conf.urls import url,include
from django.contrib import admin

urlpatterns = [
    url(r'^', include('acmeplayapp.urls')),
    url('admin/', admin.site.urls),
]
