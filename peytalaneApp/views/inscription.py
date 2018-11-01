from django.shortcuts import render
from django.http import Http404,HttpResponse,HttpResponseRedirect
from django.views import View
from django.urls import reverse

from peytalaneApp.forms import InscriptionExtForm,InscriptionEistiForm
from peytalaneApp.functions.arel import Arel
from peytalaneApp.functions.core import CoreRequest
from peytalaneApp.forms import LoginForm



class Inscription(View):
    def get(self, request, *args):
        if request.user.is_authenticated:
            return HttpResponseRedirect(reverse('reservation'))
        else:
            form = InscriptionExtForm()
            formEisti =  InscriptionEistiForm()
            return render(request,'peytalaneApp/inscription.html',locals())


    def post(self,request,*args):
        form = InscriptionExtForm(request.POST)
        formEisti = InscriptionEistiForm(request.POST)
        core = CoreRequest()

        if form.is_valid(): #form exterieurs
            username = form.cleaned_data['lastName']+form.cleaned_data['firstName']
            username = username[0:10]
            if(form.cleaned_data['password'] == form.cleaned_data['passwordConfirm']):
                if(core.add_user(
                    username.lower(),
                    form.cleaned_data['firstName'],
                    form.cleaned_data['lastName'],
                    form.cleaned_data['mail'],
                    form.cleaned_data['password'])): # we try to add user to the lpmng-core

                    #redirect to login page with username info
                    form = LoginForm()
                    info = "Inscrit ! Ton pseudo est "+username.lower()
                    return render(request, 'peytalaneApp/login.html', locals())
                else:
                    error = "Erreur n'êtes vous pas déjà inscrit en tant que "+username.lower()+"?"
                    return render(request,'peytalaneApp/inscription.html',locals())
            else:
                error = "Les deux mots de passe ne correspondent pas"
                return render(request,'peytalaneApp/inscription.html',locals())
        elif formEisti.is_valid(): # form eistiens
            arel = Arel()
            username = formEisti.cleaned_data['username']
            password = formEisti.cleaned_data['password']
            token = arel.get_token(username,password) #request to get token for arel

            if (token):
                rep_arel = arel.requete_arel('api/me',token) #request to get infos for user
                nom = rep_arel['lastName']
                prenom = rep_arel['firstName']
                email = rep_arel['email']
                if(core.add_user(username,prenom,nom,email,password)): # we try to add user to the lpmng-core
                    form = LoginForm()
                    info = "Inscrit ! Ton pseudo est "+username
                    return render(request,'peytalaneApp/login.html', locals())
                else:
                    erreur = "Erreur n'êtes vous pas déjà inscrit?"
                    return render(request,'peytalaneApp/inscription.html',locals())


            else:
                error = "Utilisateur ou mot de passe incorrect"
                return render(request,'peytalaneApp/inscription.html',locals())
        error = "Tous les champs sont obligatoires"
        return render(request,'peytalaneApp/inscription.html',locals())
        