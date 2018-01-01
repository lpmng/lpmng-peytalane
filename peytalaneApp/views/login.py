from django.views import View
from django.shortcuts import render, redirect
from peytalaneApp.forms import LoginForm
from django.http import HttpResponse
from peytalaneApp.functions.core import CoreRequest

class Login(View):
    html = 'peytalaneApp/login.html'

    """
        Renvoie la page d'Inscription au chargement de la page
    """
    def get(self, request, *args, **kwargs):
        form = LoginForm()
        return render(request, self.html, locals())

    def post(self,request,*args):
        core = CoreRequest()
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = core.logUser(username,password)
            if(user):
                print(user)
                request.session['username'] = user['uid']
                request.session['lastname'] = user['surname']
                request.session['firstname'] = user['commonname']
                return render(request,'peytalaneApp/index.html',locals())
            else:
                return render(request,self.html,locals())

        return HttpResponse('Unauthorized', status=401)

