from django import forms
from .models import Job

class NewJobForm(forms.ModelForm):
    class Meta:
        model=Job
        fields= '__all__'