from django.conf.urls import include, url

from views import user_login, user_logout, user_register

urlpatterns = [
    url(r'^login/$', user_login, name ='upload'),
    url(r'^register/$', user_register, name = "register"),
    url(r'^logout/$', user_logout, name = "logout"),
]
