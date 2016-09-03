# coding = utf-8

from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'home.html')
    # return HttpResponse('home.html')
    # return HttpResponse("<html><body>This is homepage of this website - My Task.</body></html>")