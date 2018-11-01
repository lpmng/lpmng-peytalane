from django.http import HttpResponseRedirect
from django.urls import reverse
from peytalaneApp.models_dir.user import User
from django.http import HttpResponse


def IsLogin(function):
    """
        Décorateur qui verifie que l'utilisateur est connecté.
        Passe en paramètre de la vue differentes infos sur l'utilisateur dans cet ordre:
            * si la lan a déjà été reservé
            * la liste des aliments déjà payés par l'utilisateur
            * la liste des tournois déjà payés par l'utilisateur
            * si l'utilisateur est admin
            * le total en euro du panier (penser à le recalculer dans la vue après l'ajout d'un élément dans le panier

        Utilisation :

        ```
        @IsLogin
        def get(self, request,lan_is_reserved,have_foods,have_tournament,is_admin,total, *args, **kwargs):
        ```

    """
    def wrap(self,request, *args, **kwargs):
        print(request.user)
        if request.user.is_authenticated:
            user = request.user
                        
            #it's ugly but it permits to bypass *args functionment
            if user.lan:
                lan_is_reserved = 1
            else:
                lan_is_reserved = 0
            
            is_admin = user.admin
            
            transactions_list = request.session['transactions']
            total = sum(transactions_list[key]['price'] for key in transactions_list)            
            
            have_foods = user.payment_set.filter(type_product = "food") #[elem.food for elem in user.Payment_set.all()]
            have_tournament = user.payment_set.filter(type_product = "tournament") #[elem.food for elem in user.Payment_set.all()]

            return function(self,request,lan_is_reserved,have_foods,have_tournament,is_admin,total, *args, **kwargs)
        else:
            return HttpResponseRedirect(reverse('login'))
    wrap.__doc__ = function.__doc__
    wrap.__name__ = function.__name__
    return wrap

"""
    Décorateur qui verifie que l'utilisateur est admin.
    Passe les même paramètres que le décorateur IsLogin à savoir  
            * si la lan a déjà été reservé
            * la liste des aliments déjà payés par l'utilisateur
            * la liste des tournois déjà payés par l'utilisateur
            * si l'utilisateur est admin (toujours égale à True ici)
            * le total en euro du panier (penser à le recalculer dans la vue après l'ajout d'un élément dans le panier
"""
def IsAdmin(function):
    def wrap(self, request,lan_is_reserved,have_foods,have_tournament,is_admin,total, *args, **kwargs):
        if is_admin:
            return function(self,request,lan_is_reserved,have_foods,have_tournament,is_admin,total, *args, **kwargs)
        else:
            return HttpResponse('Forbidden', status=403)

    wrap.__doc__ = function.__doc__
    wrap.__name__ = function.__name__
    return wrap