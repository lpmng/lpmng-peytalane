from django.views import View
from django.shortcuts import render, redirect
from django.http import HttpResponse
from peytalaneApp.functions.transaction import Transaction
from peytalaneApp.models_dir.tournament import *

#pages après le login
class Reservation_tournament(View):
    html = 'peytalaneApp/reservation-tournament.html'

    """
        Renvoie la page d'Inscription au chargement de la page
    """
    def get(self, request, *args, **kwargs):
        transactions_list = request.session['transactions']

        tournaments_list = Tournament.objects.all()

        print(tournaments_list)

        if 'id_tournament' in request.GET:
            self.add_tournament(0)

        return render(request, self.html, locals())

    def post(self,request,*args, **kwargs):
        user = User.objects.get(username = request.session['username'])
        # if inscription without tournament...
        if('no-tournament' in request.POST):
            if self.inscription_lan(user,request):
                success = "Inscription ajouté au panier"
            else:
                error = "Inscription non ajouté au panier"
        elif( 'tournoi' in request.POST and 'pseudo' in request.POST): # inscription with tournament
            success = self.add_tournament(request.POST['tournoi'][0],request.POST['pseudo'][0],user,request)
        else:
            error = "Les données envoyés ne sont pas valide"

        tournaments_list = Tournament.objects.all()
        transactions_list = request.session['transactions']
        return render(request, self.html, locals())

    
    def inscription_lan(self,user,request):
        
        if not user.lan:
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




    def add_tournament(self,id,pseudo,user,request):
        self.inscription_lan(user,request)
        return "Réservation ajouté dans le panier"