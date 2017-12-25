from django.shortcuts import render
from django.http import HttpResponse
from peytalaneApp.forms import InscriptionExtForm,InscriptionEistiForm

def inscription(request):
    form = InscriptionExtForm()
    formEisti =  InscriptionEistiForm()
    return render(request,'peytalaneApp/inscription.html',locals())