from django.shortcuts import render
from django.http import HttpResponse
from peytalaneApp.forms import InscriptionExtForm,InscriptionEistiForm

def index(request):
    return render(request,'peytalaneApp/index.html',locals())