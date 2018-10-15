from django.views import View
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from peytalaneApp.functions.transaction import Transaction
from peytalaneApp.models_dir.tournament import *
from peytalaneApp.functions.decorator import IsLogin


#pages après le login
class Reservation_tournament(View):
    html = 'peytalaneApp/reservation-index.html'

    """
        Renvoie la page d'Inscription au chargement de la page
    """
    @IsLogin
    def get(self, request,lan_is_reserved,have_foods,have_tournament,is_admin,total, *args, **kwargs):
        user = User.objects.get(username = request.session['username'])
        if self.inscription_lan(user,request):
            return HttpResponseRedirect("/reservation?lan=true")
        else:
            return HttpResponseRedirect("/reservation?lan=false")


    '''
    @IsLogin
    def post(self,request,lan_is_reserved,have_foods,have_tournament,is_admin,total,*args, **kwargs):
        user = User.objects.get(username = request.session['username'])
        # if inscription without tournament...
        if(have_tournament):
            error = "Vous êtes déjà inscrit sur un tournoi"
        elif('no-tournament' in request.POST):
            
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
    '''
    #add transaction to book the lan
    def inscription_lan(self,user,request):

        if not user.lan:
            Transaction.clean_transaction(request,"lan")           
            Transaction.new_transaction(
                request,
                4,
                "Réservation lan",
                "lan",
                {"user":user.username,}
            )
            return True
        else:
            return False


    #add transaction to book access to tournament
    def add_tournament(self,tournament,pseudo,user,request):
        Transaction.clean_transaction(request,"tournament")           
        Transaction.new_transaction(
            request,
            0,
            "inscription tournoi "+tournament.name,
            "tournament",
            {"user":user.username,"pseudo":pseudo,"id_tournament":tournament.id}
        )
        return "Réservation ajoutée dans le panier"