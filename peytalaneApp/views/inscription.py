from django.shortcuts import render
from django.http import Http404,HttpResponse
from peytalaneApp.forms import InscriptionExtForm,InscriptionEistiForm
from django.views import View
from peytalaneApp.functions.arel import Arel
from peytalaneApp.functions.core import CoreRequest


class inscription(View):
    def get(self, request, *args):
        form = InscriptionExtForm()
        formEisti =  InscriptionEistiForm()
        return render(request,'peytalaneApp/inscription.html',locals())


    def post(self,request,*args):
        form = InscriptionExtForm(request.POST)
        formEisti = InscriptionEistiForm(request.POST)

        if form.is_valid(): #form exterieurs
            return HttpResponse('Unauthorized', status=401)
        elif formEisti.is_valid(): # form eistiens
            arel = Arel()
            core = CoreRequest()

            username = formEisti.cleaned_data['username']
            password = formEisti.cleaned_data['password']
            token = arel.get_token(username,password) #request to get token for arel

            if (token):
                rep_arel = arel.requete_arel('api/me',token) #request to get infos for user
                nom = rep_arel['lastName']
                prenom = rep_arel['firstName']
                email = rep_arel['email']
                if(core.addUser(username,prenom,nom,email,password)): # we try to add user to the lpmng-core
                    return render(request,'peytalaneApp/index.html',locals())
                else:
                    return render(request,'peytalaneApp/inscription.html',locals())


            else:
                return HttpResponse('Unauthorized', status=401)
        print("toto")
        raise Http404