from django.views import View
from django.shortcuts import render, redirect
from django.http import HttpResponse
from peytalaneApp.functions.transaction import Transaction
from peytalaneApp.functions.decorator import IsLogin
from peytalaneApp.models_dir.food import *
from peytalaneApp.functions.transaction import Transaction


#pages après le login
class Reservation(View):
    html = 'peytalaneApp/reservation-index.html'
    
    """
        Renvoie la page d'Inscription au chargement de la page
    """
    @IsLogin
    def get(self, request,lan_is_reserved,have_foods,have_tournament,is_admin,total, *args, **kwargs):
        if "p" in request.GET:
            ok_payment = True

        if "lan" in request.GET:
            if request.GET["lan"] == "true":
                ok_lan = True
            else:
                not_ok_lan = True
        transactions_list = request.session['transactions']
        return render(request, self.html, locals())
    
    @IsLogin
    def delete(self, request,lan_is_reserved,have_foods,have_tournament,is_admin,total, *args, **kwargs):
        if "id" in request.GET:
            Transaction.delete_transaction(request,request.GET['id'])
            return HttpResponse()
        return HttpResponse('Bad request', status=400)
