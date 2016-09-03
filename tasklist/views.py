from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def upload(request):
    return HttpResponse("<html><body>This is to upload of tasklist.</body></html>")

def show(request):
    return HttpResponse("<html><body>This is show of tasklist.</body></html>")