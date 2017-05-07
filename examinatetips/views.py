from django.shortcuts import render, redirect
from django.http import HttpResponse

from django.contrib.auth.decorators import login_required

from models import ExaminateTip, TipCategory

# Create your views here.
@login_required
def upload(request):
    tipCtgr = TipCategory.objects.get_or_create(categoryName = request.POST.get('tipCategory', False))
    if request.POST.get('tipContent', False) == '' : 
        return redirect('/examinatetips/show/')
    else : 
        tip = ExaminateTip.objects.get_or_create(tipCategory = tipCtgr[0], \
            tipContent = request.POST.get('tipContent', False), \
            theExaminer = request.user)    
        return render(request, 'upload.html', { \
            'tips' : ExaminateTip.objects.filter(tipCategory = tipCtgr[0]), \
            'user' : request.user})


def show(request):
    tips = ExaminateTip.objects.all()
    return render(request, 'show.html', {'tips': tips})

