from django.conf.urls import include, url

from tasklist import views

urlpatterns = [
    url(r'upload/', views.upload, name ='upload'),
    url(r'show/', views.show, name = "show tasklist"),
]
