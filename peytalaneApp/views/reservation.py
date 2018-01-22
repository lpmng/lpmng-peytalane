from django.views import View
from django.shortcuts import render, redirect
from django.http import HttpResponse
from peytalaneApp.functions.transaction import Transaction
from peytalaneApp.models_dir.food import *

#pages après le login
class Reservation(View):
    html = 'peytalaneApp/reservation-index.html'
    
    """
        Renvoie la page d'Inscription au chargement de la page
    """
    def get(self, request, *args, **kwargs):
<<<<<<< HEAD
        t = Transaction(10,"Pizza 4 fromages Grande",None)
        t2 = Transaction(4,"Payement lan non cotisant",None)
        transactions_list = [t,t2]
        print(t.price)
        return render(request, self.html, locals())
=======
        transactions_list = request.session['transactions']
        return render(request, self.html, locals())
>>>>>>> f04fc667f519533bd00ec9ba96d9d2906de84bfd
