from django.views import View
from django.shortcuts import render, redirect
from peytalaneApp.forms import LoginForm

class login(View):
    # page d'acceuil, de connexion, d'inscription
    html = 'peytalaneApp/login.html'

    """
        Renvoie la page d'Inscription au chargement de la page
    """
    def get(self, request, *args, **kwargs):
        form = LoginForm()
        return render(request, self.html, locals())
