from django.views import View
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth import authenticate,login

from peytalaneApp.forms import LoginForm
from peytalaneApp.functions.core import CoreRequest
from peytalaneApp.models_dir.user import User

class Login(View):
    html = 'peytalaneApp/login.html'

    """
        Renvoie la page d'Inscription au chargement de la page
    """
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
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
            user = authenticate(username=username, password=password, request=request)
            if(user):
                login(request,user)
                return HttpResponseRedirect(reverse('reservation'))
            else:
                error = "Utilisateur ou mot de passe invalide"
                return render(request,self.html,locals())

        return HttpResponse('Unauthorized', status=401)

