from django.views import View
from django.shortcuts import render, redirect
from peytalaneApp.forms import LoginForm
from django.http import HttpResponse

class login(View):
    html = 'peytalaneApp/login.html'

    """
        Renvoie la page d'Inscription au chargement de la page
    """
    def get(self, request, *args, **kwargs):
        form = LoginForm()
        return render(request, self.html, locals())

    def post(self,request,*args):
        return HttpResponse('Unauthorized', status=401)

