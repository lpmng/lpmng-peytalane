from django.views import View
from django.shortcuts import render, redirect
from peytalaneApp.forms import LoginForm
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from peytalaneApp.functions.core import CoreRequest
from peytalaneApp.models_dir.user import User

class Login(View):
    html = 'peytalaneApp/login.html'

    """
        Renvoie la page d'Inscription au chargement de la page
    """
    def get(self, request, *args, **kwargs):
        if('username' in request.session):
            return HttpResponseRedirect(reverse('reservation'))
        else:
            form = LoginForm()
            return render(request, self.html, locals())

    def post(self,request,*args):
        core = CoreRequest()
        form = LoginForm(request.POST)
        error = ""
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = core.logUser(username,password)
            if(user):
                # we save connected user 
                request.session['username'] = username
                request.session['token'] = user['token']
                #info_user = core.requete_core_get("/users/"+username+"/isadmin",user['token'])
                #print(info_user)
                request.session['transactions'] = dict()
                request.session["transactions_max_id"] = 0


                # if user doesn't exist in bdd we create it
                obj, created  = User.objects.get_or_create(username=username)
                return HttpResponseRedirect(reverse('reservation'))
            else:
                error = "Utilisateur ou mot de passe invalide"
                return render(request,self.html,locals())

        return HttpResponse('Unauthorized', status=401)

