from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return render(request,'peytalaneApp/index.html',locals())

def inscription(request):
    return render(request,'peytalaneApp/inscription.html',locals())