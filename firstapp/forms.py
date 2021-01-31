from django import forms
from .models import Job

class Jobform(forms.ModelForm):
    class Meta:
        model = Job
        fields = [
            'meta',
            'apps',
            'playlist',
            'jobtype',
            'sp'
        ]