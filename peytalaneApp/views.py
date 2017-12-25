from django.shortcuts import render
from django.http import HttpResponse
from .forms import InscriptionExtForm,InscriptionEistiForm
# Create your views here.

def index(request):
    return render(request,'peytalaneApp/index.html',locals())

def inscription(request):
    form = InscriptionExtForm()
    formEisti =  InscriptionEistiForm()
    return render(request,'peytalaneApp/inscription.html',locals())