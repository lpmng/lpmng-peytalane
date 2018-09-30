from django.views import View
from django.shortcuts import render
from django.middleware.csrf import CsrfViewMiddleware

from peytalaneApp.functions.transaction import Transaction
from peytalaneApp.models_dir.food import Food
from peytalaneApp.models_dir.food import ValueOption
from peytalaneApp.models_dir.user import User
from peytalaneApp.functions.decorator import IsLogin
from peytalaneApp.models_dir.payment import Payment,Payment_option

# pages après sélection de l'option choix nourriture


class Reservation_admin(View):
    """
        Renvoi la page de sélection des pizzas
    """
    RENDER_HTML = 'peytalaneApp/reservation-admin.html'
    @IsLogin
    def get(self, request,lan_is_reserved,have_foods,have_tournament, *args, **kwargs):
        transactions_list = request.session['transactions']
        payment_list_object = Payment.objects.all()
        #payment_list = [ payment for payment in payment_list_object]
        return render(request, self.RENDER_HTML, locals())
