from django.conf.urls import include, url

from examinatetips import views

urlpatterns = [
    url(r'^$', views.show, name = "show examination tips"),
    url(r'^upload/', views.upload, name ='upload'),
    url(r'^show/', views.show, name = "show examination tips"),
]
