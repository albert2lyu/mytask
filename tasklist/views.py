from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template.loader import get_template
from django.contrib.auth.decorators import login_required

from tasklist.models import PatentItem 
from .form import PatentItemForm

# Create your views here.

@login_required
def upload(request):
    if request.method == 'POST':
        form = PatentItemForm(request.POST)
        if form.is_valid():
            form.save(commit = False)
            form.theExaminer = request.user.id
            form.save()
            return HttpResponseRedirect('/tasklist/show/')
        
    update_form = PatentItemForm
    return render(request, 'upload.html', {'update_form' : update_form})



def show(request):
    patents = PatentItem.objects.all().order_by('appDate')[:10]
    return render(request, 'show.html', {'records' : patents})
