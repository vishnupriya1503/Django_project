from django import forms
from .models import BusTiming
import datetime

class BusTimingForm(forms.ModelForm):
    class Meta:
        model = BusTiming
        fields = '__all__'


