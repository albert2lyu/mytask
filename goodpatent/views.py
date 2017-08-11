from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404

from django.contrib.auth.decorators import login_required

from .models import GoodPatent

# Create your views here.
def show(request, pk) : 
    gp = get_object_or_404(GoodPatent, pk = pk)
    gps = GoodPatent.objects.all()[0:5]
    
    return render(request, 'show_goodpatent.html', {'gp': gp, 'gps': gps})
