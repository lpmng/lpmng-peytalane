from django.views import View
from django.shortcuts import render, redirect
from django.http import HttpResponse
from peytalaneApp.functions.transaction import Transaction
from peytalaneApp.models_dir.food import *
from peytalaneApp.models_dir.user import User

#pages après sélection de l'option choix nourriture

class Reservation_food(View):
    html = 'peytalaneApp/reservation-food.html'

    """
        Renvoi la page de sélection des pizzas
    """
    def get(self, request, *args, **kwargs):
        transactions_list = request.session['transactions']
        pizzas_list = Food.objects.all()
        for a in pizzas_list:
            for b in a.options.all():
                print(b.name)

                
        return render(request, self.html, locals())
    def post(self, request, *args, **kwargs):
        user = User.objects.get(username = request.session['username'])
        pizzas_list = Food.objects.all()
        print(request.POST)
        if (request.POST["Taille"] == '1'):
            taille =" Grande"
            prix = 10
        else:
            prix = 7
            taille = " Petite"
        transaction_obj = { 
            "price":prix,
            "product":request.POST["pizzaName"]+taille,
            "action_payment":"food",
            "args":{"user":user.username,"id_food":request.POST["pizzaId"],"taille":request.POST["Taille"],"base":request.POST["Base"]}
        }
        transactions_list = request.session['transactions']
        transactions_list.append(transaction_obj)
        request.session['transactions'] = transactions_list
        return render(request, self.html, locals())
