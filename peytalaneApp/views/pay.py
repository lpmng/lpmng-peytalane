from django.views import View
from django.shortcuts import render, redirect
from django.http import HttpResponse
from peytalaneApp.functions.transaction import Transaction
from peytalaneApp.models_dir.tournament import *
from peytalaneApp.functions.decorator import IsLogin
from django import forms
from django.shortcuts import redirect

class Pay(View):
    html = 'peytalaneApp/pay.html'


    @IsLogin
    def get(self, request,lan_is_reserved,have_foods, *args, **kwargs):
        transactions_list = request.session['transactions']
        tournaments_list = Tournament.objects.all()
        total = sum(transactions['price'] for transactions in transactions_list)
        return render(request, self.html, locals())


    @IsLogin
    def post(self,request,*args, **kwargs):
        transactions_list = request.session['transactions']
        for transaction in request.session['transactions']:
            payment = Transaction(**transaction)
            print("toto")
            payment.payment()
            del transaction

        '''
        total = sum(transactions['price'] for transactions in transactions_list)
        if('telephone' in request.POST and request.POST['telephone'] != ''):
            truc=pay.lydia(total, request.POST['telephone'])
            return redirect(truc['mobile_url'])
            del truc

            del request.session['transactions']
            request.session.modified = True
        else:
            error = "Entrez un numéro de telephone"
        '''

        return render(request, self.html, locals())
