from django.shortcuts import render, redirect
from django.http import HttpResponse

from models import ExaminateTip, TipCategory

# Create your views here.
def upload(request):
    tipCtgr = TipCategory.objects.get_or_create(categoryName = request.POST.get('tipCategory', False))
    tip = ExaminateTip.objects.get_or_create(tipCategory = tipCtgr[0], \
        tipContent = request.POST.get('tipContent', False))
    
    return render(request, 'upload.html', {'tips' : ExaminateTip.objects.filter(tipCategory = tipCtgr[0])})


def show(request):
    tips = ExaminateTip.objects.all()
    return render(request, 'show.html', {'tips': tips})

