from django.views import View
from django.shortcuts import render, redirect
from django.http import HttpResponse
from peytalaneApp.functions.transaction import Transaction
from peytalaneApp.models_dir.tournament import *

#pages après le login
class Reservation_tournament(View):
    html = 'peytalaneApp/reservation-tournament.html'

    """
        Renvoie la page d'Inscription au chargement de la page
    """
    def get(self, request, *args, **kwargs):
        t = Transaction(10,"Pizza 4 fromages Grande",None)
        t2 = Transaction(4,"Payement lan non cotisant",None)
        transactions_list = [t,t2]

        tournaments_list = Tournament.objects.all()

        print(tournaments_list)

        if 'id_tournament' in request.GET:
            self.add_tournament(0)

        return render(request, self.html, locals())

    def post(self,request,*args, **kwargs):
        print(request.POST)
        tournaments_list = Tournament.objects.all()
        return render(request, self.html, locals())


    def add_tournament(self,id):
        print('plop')