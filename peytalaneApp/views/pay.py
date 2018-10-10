from django.views import View
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from peytalaneApp.functions.transaction import Transaction
from django.urls import reverse
from peytalaneApp.models_dir.tournament import *
from peytalaneApp.functions.decorator import IsLogin
from django import forms
from django.shortcuts import redirect
import stripe
import json
import os



BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

class Pay(View):
    html = 'peytalaneApp/pay.html'


    @IsLogin
    def get(self, request,lan_is_reserved,have_foods,is_admin, *args, **kwargs):
        json_data=open(BASE_DIR+'/keyStripe.json')
        data = json.load(json_data)
        key = data["public"]
        transactions_list = request.session['transactions']
        tournaments_list = Tournament.objects.all()
        total = sum(transactions_list[key]['price'] for key in transactions_list)
        total_cent = total * 100
        return render(request, self.html, locals())

    @IsLogin
    def post(self,request,*args, **kwargs):
        json_data=open(BASE_DIR+'/keyStripe.json')
        data = json.load(json_data)
        if 'stripeToken' in request.POST:
            transactions_list = request.session['transactions']
            total = sum(transactions_list[key]['price'] for key in transactions_list)


            stripe.api_key = data['private']

            # Token is created using Checkout or Elements!
            # Get the payment token ID submitted by the form:
            token = request.POST['stripeToken']
            try:
                charge = stripe.Charge.create(
                    amount=total*100,
                    currency='eur',
                    description='peytalane test',
                    source=token,
                )
            except Exception as e:
                error = str(e)
                return render(request, self.html, locals())

            if charge.paid:
                for transaction_key in transactions_list.keys():
                    transaction = Transaction(**request.session['transactions'][transaction_key])
                    transaction.payment()
            
                request.session['transactions'] = dict()
                request.session.modified = True
                transactions_list = request.session['transactions']
                return HttpResponseRedirect("/reservation?p=plouf")
            else:
                error = "Le payement a échoué"
                return render(request, self.html, locals())
        else:
            error = "L'api de payement n'a pas été contacté, il ne s'est rien passé"
            return render(request, self.html, locals())



