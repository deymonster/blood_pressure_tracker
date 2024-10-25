from django import forms
from .models import BloodPressureRecord

class BloodPressureForm(forms.ModelForm):
    class Meta:
        model = BloodPressureRecord
        fields = ['systolic', 'diastolic']