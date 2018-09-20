from django.views import View
from django.shortcuts import render

from peytalaneApp.functions.transaction import Transaction
from peytalaneApp.models_dir.food import Food
from peytalaneApp.models_dir.food import ValueOption
from peytalaneApp.models_dir.user import User
from peytalaneApp.functions.decorator import IsLogin


# pages après sélection de l'option choix nourriture


class Reservation_food(View):
    """
        Renvoi la page de sélection des pizzas
    """
    RENDER_HTML = 'peytalaneApp/reservation-food.html'
    @IsLogin
    def get(self, request,lan_is_reserved,have_foods, *args, **kwargs):
        transactions_list = request.session['transactions']
        print(transactions_list)
        pizzas_list = Food.objects.all()
        return render(request, self.RENDER_HTML, locals())
    

    @IsLogin
    def post(self, request, *args, **kwargs):
        user = User.objects.get(username=request.session['username'])
        
        print(request.POST)

        selected_pizza = Food.objects.get(id = request.POST["pizzaId"])
        
        options = request.POST.copy()
        del options['csrfmiddlewaretoken']
        del options['pizzaId']
        del options['pizzaName']

        price = selected_pizza.price

        args_transaction = dict()
        args_transaction["id_food"] = request.POST["pizzaId"]
        args_transaction["options"] = options.copy()
        args_transaction["user"] = user.username

        product_name = request.POST["pizzaName"]

        for options_key in options.keys():
            selected_value = ValueOption.objects.get(id = options[options_key])
            product_name = product_name + "<br/>" + options_key + ":" + selected_value.value
            price = price + selected_value.price
        
        transaction_obj = {
            "price": price,
            "product": product_name,
            "action_payment": "food",
            "args": args_transaction
        }
        transactions_list = request.session['transactions']
        transactions_list.append(transaction_obj)
        request.session['transactions'] = transactions_list
        return render(request, self.RENDER_HTML, locals())
