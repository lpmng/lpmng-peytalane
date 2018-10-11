from django.views import View
from django.shortcuts import render
from django.middleware.csrf import CsrfViewMiddleware
from django.http import HttpResponse
from django.db.models import Q
import csv

from peytalaneApp.functions.transaction import Transaction
from peytalaneApp.models_dir.food import Food
from peytalaneApp.models_dir.food import ValueOption
from peytalaneApp.models_dir.user import User
from peytalaneApp.models_dir.tournament import *
from peytalaneApp.functions.decorator import IsLogin,IsAdmin
from peytalaneApp.models_dir.payment import Payment,Payment_option,Payment_option_value
from peytalaneApp.functions.core import *
# pages après sélection de l'option choix nourriture



class Food_csv(View):
    @IsLogin
    @IsAdmin
    def get(self, request,lan_is_reserved,have_foods,have_tournament,is_admin,total, *args, **kwargs):
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="somefilename.csv"'
        list_food = Payment.objects.filter(Q(product__contains="Pizza"))
        list_options = list(set(Payment_option.objects.filter(payment__in=list_food)))
        
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="somefilename.csv"'

        writer = csv.writer(response)

        first_line = ["Nombre"] + list_options + ["Nom","Commentaire"]
        writer.writerow(first_line)

        for food in list_food:
            print("plouf")
            line = []
            line.append(1)
            for option in list_options:
                try:
                    line.append(Payment_option_value.objects.get(option=option,payment=food).value)
                except Payment_option_value.DoesNotExist:
                    line.append("X")
            line.append(food.product)
            line.append(food.comment.strip())

            writer.writerow(line)

        return response
            


    def agregate_food(self,list_food):
        raise NotImplemented





class Food_admin(View):
    """
        Renvoi la page d'admin de la nourriture
    """
    RENDER_HTML = 'peytalaneApp/admin/food.html'
    @IsLogin
    @IsAdmin
    def get(self, request,lan_is_reserved,have_foods,have_tournament,is_admin,total, *args, **kwargs):
        transactions_list = request.session['transactions']
        list_food = Payment.objects.filter(type_product = "food")
        list_options = Payment_option.objects.all()
        menu_selected_element = "food"

        core = CoreRequest()
        core.add_session(request)
        return render(request, self.RENDER_HTML, locals())

    @IsLogin
    @IsAdmin
    def put(self, request,lan_is_reserved,have_foods,have_tournament,is_admin,total, *args, **kwargs):
        if "id" in request.GET:
            payment_tmp = Payment.objects.get(id = request.GET['id'])
            if "delivered" in request.GET:
                if request.GET["delivered"] == "1":
                    payment_tmp.delivered = True
                    payment_tmp.save()
                elif request.GET["delivered"] == "0":
                    payment_tmp.delivered = False
                    payment_tmp.save()
                else:
                    return HttpResponse('Bad request', status=400)
                return HttpResponse()

        return HttpResponse('Bad request', status=400)


class User_admin(View):
    """
        Renvoi la page d'admin des utilisateurs
    """
    RENDER_HTML = 'peytalaneApp/admin/users.html'
    
    @IsLogin
    @IsAdmin
    def get(self, request,lan_is_reserved,have_foods,have_tournament,is_admin,total, *args, **kwargs):
        
        list_user = User.objects.all()
        menu_selected_element = "user"
        return render(request, self.RENDER_HTML, locals())

    @IsLogin
    @IsAdmin
    def put(self, request,lan_is_reserved,have_foods,have_tournament,is_admin,total, *args, **kwargs):
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
    @IsAdmin
    def get(self, request,lan_is_reserved,have_foods,have_tournament,is_admin, *args, **kwargs):
        list_tournament = Tournament.objects.all()
        menu_selected_element = "tournament"
        return render(request, self.RENDER_HTML, locals())
