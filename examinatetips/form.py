from django.forms import ModelForm
from .models import TipCategory, ExaminateTip

class ExaminateTipForm(ModelForm):
    class Meta:
        model = ExaminateTip
        exclude = ['theExaminer', 'submitTime']