from django.views import View
from django.shortcuts import render

from peytalaneApp.functions.transaction import Transaction
from peytalaneApp.models_dir.food import Food
from peytalaneApp.models_dir.user import User
from peytalaneApp.functions.decorator import IsLogin


# pages après sélection de l'option choix nourriture


class Reservation_food(View):
    """
        Renvoi la page de sélection des pizzas
    """
    RENDER_HTML = 'peytalaneApp/reservation-food.html'
    @IsLogin
    def get(self, request, *args, **kwargs):
        transactions_list = request.session['transactions']
        pizzas_list = Food.objects.all()
        return render(request, self.RENDER_HTML, locals())
    

    @IsLogin
    def post(self, request, *args, **kwargs):
        user = User.objects.get(username=request.session['username'])
        pizzas_list = Food.objects.all()
        if request.POST["Taille"] == '1':
            taille = " Grande"
            prix = 10
        else:
            prix = 7
            taille = " Petite"
        transaction_obj = {
            "price": prix,
            "product": request.POST["pizzaName"] + taille,
            "action_payment": "food",
            "args": {"user": user.username,
                     "id_food": request.POST["pizzaId"],
                     "taille": request.POST["Taille"]}
        }
        transactions_list = request.session['transactions']
        transactions_list.append(transaction_obj)
        request.session['transactions'] = transactions_list
        return render(request, self.RENDER_HTML, locals())
