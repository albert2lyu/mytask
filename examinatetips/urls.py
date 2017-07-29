from django.conf.urls import include, url

from .views import upload, show

urlpatterns = [
    url(r'upload/', upload, name ='upload'),
    url(r'show/', show, name = "show examination tips"),
]
