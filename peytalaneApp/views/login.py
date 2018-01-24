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
        form = LoginForm()
        return render(request, self.html, locals())

    def post(self,request,*args):
        #core = CoreRequest()
        form = LoginForm(request.POST)
        error = ""
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            #user = core.logUser(username,password)
            if(True):
                
                # we save connected user 
                request.session['username'] = "toto"
                request.session['token'] = "bob"
                request.session['transactions'] = []

                # if user doesn't exist in bdd we create it
                obj, created  = User.objects.get_or_create(username="toto")
                return HttpResponseRedirect(reverse('reservation'))
            else:
                error = "Utilisateur ou mot de passe invalide"
                return render(request,self.html,locals())

        return HttpResponse('Unauthorized', status=401)

