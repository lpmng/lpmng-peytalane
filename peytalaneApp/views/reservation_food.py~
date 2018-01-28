from django.views import View
from django.shortcuts import render, redirect
from django.http import HttpResponse
from peytalaneApp.functions.transaction import Transaction

#pages après sélection de l'option choix nourriture

class Food():
    
    def __init__(self,name,optionList,valueOptionList):
        self.name = name
        #self.product = product
        #self.action_payment = action_payment

class Reservation_food(View):
    html = 'peytalaneApp/reservation-food.html'

    """
        Renvoi la page de sélection des pizzas
    """
    def get(self, request, *args, **kwargs):
        p1 = Food("chorizo",None,None)
        p2 = Food("4 fromages",None,None)
        pizzas_list = [p1,p2]
        return render(request, self.html, locals())
