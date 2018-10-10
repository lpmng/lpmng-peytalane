from django.shortcuts import render
from django.http import HttpResponse
from peytalaneApp.forms import InscriptionExtForm,InscriptionEistiForm

def index(request):
    if("transactions" in request.session):
        transactions_list = request.session['transactions']
        total = sum(transactions_list[key]['price'] for key in transactions_list)  
    return render(request,'peytalaneApp/index.html',locals())