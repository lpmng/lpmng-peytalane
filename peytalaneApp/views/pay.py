from django.views import View
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from peytalaneApp.functions.transaction import Transaction
from django.urls import reverse
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
        total = sum(transactions_list[key]['price'] for key in transactions_list)
        return render(request, self.html, locals())


    @IsLogin
    def post(self,request,*args, **kwargs):
        transactions_list = request.session['transactions']
        transations_keys = request.session['transactions'].keys()
        for key in transations_keys:
            payment = Transaction(**request.session['transactions'][key])
            payment.payment()

        request.session['transactions'] = dict()
        request.session.modified = True
        transactions_list = request.session['transactions']
        return HttpResponseRedirect(reverse('reservation'))