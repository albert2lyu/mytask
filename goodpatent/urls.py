from django.conf.urls import include, url
from .views import show

urlpatterns = [
    url(r'^show/(?P<pk>\d+)/$', show, name = "show_goodpatent"),
]