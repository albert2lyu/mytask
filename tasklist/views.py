from django.shortcuts import render
from django.http import HttpResponse

from tasklist.models import PatentItem 

# Create your views here.

def upload(request):
    return render(request, 'upload.html')

def show(request):
    patents = PatentItem.objects.all().order_by('appDate')[:10]
    return render(request, 'show.html', {'records' : patents})
