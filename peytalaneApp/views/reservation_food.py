from django.views import View
from django.shortcuts import render
from django.middleware.csrf import CsrfViewMiddleware
from django.http import HttpResponse

from peytalaneApp.functions.transaction import Transaction
from peytalaneApp.models_dir.food import Food
from peytalaneApp.models_dir.food import ValueOption
from peytalaneApp.models_dir.user import User
from peytalaneApp.functions.decorator import IsLogin

import pdb
import json

# pages après sélection de l'option choix nourriture


class Search_food(View):
    @IsLogin
    def get(self, request,lan_is_reserved,have_foods,have_tournament,is_admin,total, *args, **kwargs):
        if "s" in request.GET:
            pizzas_list = Food.objects.filter(name__contains=request.GET["s"])
            name_pizzas = [pizza.name for pizza in pizzas_list]
            response_data = dict()
            response_data['pizzas'] = name_pizzas
            return HttpResponse(json.dumps(response_data), content_type="application/json")

class Reservation_food(View):
    """
        Renvoi la page de sélection des pizzas
    """
    RENDER_HTML = 'peytalaneApp/reservation-food.html'
    @IsLogin
    def get(self, request,lan_is_reserved,have_foods,have_tournament,is_admin,total, *args, **kwargs):
        transactions_list = request.session['transactions']
        pizzas_list = Food.objects.all()
        return render(request, self.RENDER_HTML, locals())
    

    @IsLogin
    def post(self, request,lan_is_reserved,have_foods,have_tournament,is_admin,total, *args, **kwargs):
        pizzas_list = Food.objects.all()
        user = request.user
        
        if("pizzaId" in request.POST and "pizzaName" in request.POST):

            selected_pizza = Food.objects.get(id = request.POST["pizzaId"])
            needed_options = selected_pizza.options.all()

            for needed_option in needed_options:
                if not needed_option.name in request.POST:
                    error = "reservation refusée"
                    return render(request, self.RENDER_HTML, locals())
            
            options = request.POST.copy()
            del options['csrfmiddlewaretoken']
            del options['pizzaId']
            del options['pizzaName']
            del options['comment']

            price = selected_pizza.price

            args_transaction = dict()
            args_transaction["id_food"] = request.POST["pizzaId"]
            args_transaction["options"] = dict()
            args_transaction["user"] = user.username

            product_name = request.POST["pizzaName"]

            for options_key in options.keys():
                selected_value = ValueOption.objects.get(id = options[options_key])
                price = price + selected_value.price
                args_transaction["options"][options_key] = (options[options_key],selected_value.value)
            
            if "comment" in request.POST:
                comment = request.POST["comment"].strip()

            Transaction.new_transaction(
                request,
                price,
                product_name,
                "food",
                args_transaction,
                comment
            )
            success = "Nourriture reservé"
        else:
            error = "Réservation refusée"
        
        transactions_list = request.session['transactions']
        total = sum(transactions_list[key]['price'] for key in transactions_list)

        return render(request, self.RENDER_HTML, locals())
