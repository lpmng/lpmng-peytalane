from django.views import View
from django.shortcuts import render
from django.middleware.csrf import CsrfViewMiddleware
from django.http import HttpResponse

from peytalaneApp.functions.transaction import Transaction
from peytalaneApp.models_dir.food import Food
from peytalaneApp.models_dir.food import ValueOption
from peytalaneApp.models_dir.user import User
from peytalaneApp.models_dir.tournament import *
from peytalaneApp.functions.decorator import IsLogin
from peytalaneApp.models_dir.payment import Payment,Payment_option

# pages après sélection de l'option choix nourriture


class Food_admin(View):
    """
        Renvoi la page d'admin de la nourriture
    """
    RENDER_HTML = 'peytalaneApp/admin/food.html'
    @IsLogin
    def get(self, request,lan_is_reserved,have_foods,have_tournament,is_admin, *args, **kwargs):
        transactions_list = request.session['transactions']
        list_food = Payment.objects.filter(type_product = "food")
        list_options = Payment_option.objects.all()
        menu_selected_element = "food"
        return render(request, self.RENDER_HTML, locals())


class User_admin(View):
    """
        Renvoi la page d'admin des utilisateurs
    """
    RENDER_HTML = 'peytalaneApp/admin/users.html'
    @IsLogin
    def get(self, request,lan_is_reserved,have_foods,have_tournament,is_admin, *args, **kwargs):
        list_user = User.objects.all()
        menu_selected_element = "user"
        return render(request, self.RENDER_HTML, locals())

    @IsLogin
    def put(self, request,lan_is_reserved,have_foods,have_tournament,is_admin, *args, **kwargs):
        if "username" in request.GET:
            user_tmp = User.objects.get(username = request.GET['username'])
            if "admin" in request.GET and username != request.session['username']:
                if request.GET["admin"] == "1":
                    user_tmp.admin = True
                    user_tmp.save()
                elif request.GET["admin"] == "0":
                    user_tmp.admin = False
                    user_tmp.save()
                else:
                    return HttpResponse('Bad request', status=400)
                return HttpResponse()

        return HttpResponse('Bad request', status=400)

class Tournament_admin(View):
    """
        Renvoi la page d'admin de la nourriture
    """
    RENDER_HTML = 'peytalaneApp/admin/tournament.html'
    @IsLogin
    def get(self, request,lan_is_reserved,have_foods,have_tournament,is_admin, *args, **kwargs):
        list_tournament = Tournament.objects.all()
        menu_selected_element = "tournament"
        return render(request, self.RENDER_HTML, locals())




