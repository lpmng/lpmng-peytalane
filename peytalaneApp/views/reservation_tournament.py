from django.views import View
from django.shortcuts import render, redirect
from django.http import HttpResponse
from peytalaneApp.functions.transaction import Transaction
from peytalaneApp.models_dir.tournament import *
from peytalaneApp.functions.decorator import IsLogin


#pages après le login
class Reservation_tournament(View):
    html = 'peytalaneApp/reservation-tournament.html'

    """
        Renvoie la page d'Inscription au chargement de la page
    """
    @IsLogin
    def get(self, request,lan_is_reserved,have_foods, *args, **kwargs):
        transactions_list = request.session['transactions']

        tournaments_list = Tournament.objects.all()

        print(tournaments_list)

        if 'id_tournament' in request.GET:
            self.add_tournament(0)

        return render(request, self.html, locals())


    @IsLogin
    def post(self,request,*args, **kwargs):
        user = User.objects.get(username = request.session['username'])
        # if inscription without tournament...
        if('no-tournament' in request.POST):
            if self.inscription_lan(user,request):
                success = "Inscription ajoutée au panier"
            else:
                error = "Inscription non ajoutée au panier"
        elif not 'tournoi' in request.POST:
            error = "Veuillez selectionner un tournoi"
        elif 'pseudo' in request.POST: # inscription with tournament
            tournament = Tournament.objects.get(id = request.POST['tournoi'])
            self.inscription_lan(user,request)
            success = self.add_tournament(tournament,request.POST['pseudo'],user,request)
        else:
            error = "Les données envoyés ne sont pas valides"

        tournaments_list = Tournament.objects.all()
        transactions_list = request.session['transactions']
        return render(request, self.html, locals())

    #add transaction to book the lan
    def inscription_lan(self,user,request):

        if not user.lan:
            self.clear_transaction(request,"lan")
            transaction_obj = {
                                "price":4,
                                "product":"Réservation lan",
                                "action_payment":"lan",
                                "args":{"user":user.username,}
                              }
            transactions_list = request.session['transactions']
            transactions_list.append(transaction_obj)
            request.session['transactions'] = transactions_list
            return True
        else:
            return False


    #add transaction to book access to tournament
    def add_tournament(self,tournament,pseudo,user,request):
        self.clear_transaction(request,"tournament")
        print(pseudo)
        transaction_obj =   {
                                "price":0,
                                "product":"inscription tournoi "+tournament.name,
                                "action_payment":"tournament",
                                "args":{"user":user.username,"pseudo":pseudo,"id_tournament":tournament.id}
                            }
        transactions_list = request.session['transactions']
        transactions_list.append(transaction_obj)
        request.session['transactions'] = transactions_list
        return "Réservation ajoutée dans le panier"

    # delete all transaction where action_payment = action_payment arg
    def clear_transaction(self,request,action_payment):
        transactions_list = request.session['transactions']
        new_list = []
        for transaction_obj in transactions_list:
            if(transaction_obj["action_payment"] != action_payment):
                new_list.append(transaction_obj)

        request.session['transactions'] = new_list
