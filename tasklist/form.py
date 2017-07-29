from django.forms import ModelForm
from .models import PatentItem

class PatentItemForm(ModelForm):
    class Meta:
        model = PatentItem
        exclude = ['theExaminer']