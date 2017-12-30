from django.views import View
from django.shortcuts import render, redirect
from django.http import HttpResponse

#pages après le login
class reservation(View):
    html = 'peytalaneApp/reservation-index.html'

    """
        Renvoie la page d'Inscription au chargement de la page
    """
    def get(self, request, *args, **kwargs):
        return render(request, self.html, locals())