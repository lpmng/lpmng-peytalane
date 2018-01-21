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
        transactions_list = request.session['transactions']
        return render(request, self.html, locals())