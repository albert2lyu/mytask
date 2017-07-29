from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect

from django.contrib.auth.decorators import login_required

from models import ExaminateTip, TipCategory
from .form import ExaminateTipForm

from datetime import datetime

# Create your views here.
@login_required
def upload(request):
    # tipCtgr = TipCategory.objects.get_or_create(categoryName = request.POST.get('tipCategory', False))
    # if request.POST.get('tipContent', False) == '' : 
    #     return redirect('/examinatetips/show/')
    # else : 
    #     tip = ExaminateTip.objects.get_or_create(tipCategory = tipCtgr[0], \
    #         tipContent = request.POST.get('tipContent', False), \
    #         theExaminer = request.user)  
    #     yourtips = ExaminateTip.objects.filter(theExaminer = request.user)  
    #     return render(request, 'upload.html', { \
    #         'tips' : ExaminateTip.objects.filter(tipCategory = tipCtgr[0]), \
    #         'yourtips' : yourtips, \
    #         'user' : request.user})

    if request.method == 'POST':
        form = ExaminateTipForm(request.POST)
        if form.is_valid() : 
            form.theExaminer = request.user
            form.submitTime = datetime.now()
            form.save()
            return HttpResponseRedirect('/examinatetips/show')
    else :
        update_form = ExaminateTipForm
    return render(request, 'upload_tips.html', {'update_form': update_form, 'user': request.user})


def show(request):
    tips = ExaminateTip.objects.all()
    return render(request, 'show_tips.html', {'tips': tips})

