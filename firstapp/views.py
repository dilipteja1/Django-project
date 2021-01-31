from django.shortcuts import render
from .forms import Jobform
from .models import Job
from django.http import HttpResponse
# Create your views here.

def home_view(request,*args,**kwargs):
    job_form = Jobform(request.POST)
    if job_form.is_valid():
        job_form.save()
    context = {
        'form': job_form
    }
    return render(request , 'home.html',context)

