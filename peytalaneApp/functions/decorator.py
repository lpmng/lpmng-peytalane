from django.http import HttpResponseRedirect
from django.urls import reverse
from peytalaneApp.models_dir.user import User


def IsLogin(function):
    def wrap(self,request, *args, **kwargs):
        if('username' in request.session):
            user = User.objects.get(username = request.session['username'])
            
            #it's ugly but it permits to bypass *args functionment
            if user.lan:
                print("plop")
                lan_is_reserved = 1
            else:
                lan_is_reserved = 0
            
            
            # TODO : change it by real data
            have_foods = user.payment_set.filter(type_product = "food") #[elem.food for elem in user.Payment_set.all()]
            have_tournament = user.payment_set.filter(type_product = "tournament") #[elem.food for elem in user.Payment_set.all()]

            return function(self,request,lan_is_reserved,have_foods,have_tournament, *args, **kwargs)
        else:
            return HttpResponseRedirect(reverse('login'))
    wrap.__doc__ = function.__doc__
    wrap.__name__ = function.__name__
    return wrap
