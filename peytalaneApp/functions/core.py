
import os
import json
import requests

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


class CoreRequest():
    "Module pour la gestion des requètes sur LPMNG-Core"

    urlCore = "http://127.0.0.1:8001"

    def get_token(self,user,pwd):
        """
            Recupère un token de l'api du Core si le user et le mot de passe correspondent
        """
        #on charge les identifiants pour se connecter à l'api du core (il faudrait faire un try catch...)
        json_data=open(BASE_DIR+'/keyCore.json')
        if(json_data):
            data = json.load(json_data)
            key = data['key']
            app = data['app']
            data = {
                        'grant_type':'password',
                        'username':user,
                        'password':pwd,
                        'scope':'read',
                        'format':'json'
                    }
            # on envoi la requete et on la recupere en json.
            http_response = requests.post(self.urlCore+'/o/token/', data = data,auth=(app, key))
            # throw une json.decoder.JSONDecodeError en cas de mauvais identifiants
            http_response_json = http_response.json()
            # si on recoit un token c'est bon
            if ('access_token' in http_response_json.keys()):
                return http_response_json['access_token']
        return False

    def add_session(self,request):
        """
            Fait une requète pour donner une session à l'utilisateur qui est connecté
        """
        token = request.session["token"]
        username = request.user.username
        req = self.requete_core_get("/users/"+username+"/",token)
        req['nbSessions'] = 1
        headers = {'Accept':'application/json','AUTHORIZATION':'Bearer '+token}
        http_response = requests.patch(self.urlCore+"/users/"+username+"/",headers = headers,data=req)



    def requete_core_get(self,url_api,token):
        """
            Fait une requète sur l'api du Core et renvoi le résultat en Json (le token doit être valide)

            * url_api : url sur laquelle la requète doit être faite
            * token : token d'un utilisateur identifié

        """
        headers = {'Accept':'application/json','AUTHORIZATION':'Bearer '+token}
        data = {
                'format':'json',
            }
        http_response = requests.get(self.urlCore+url_api,headers = headers,data=data)
        if http_response.status_code == 200:
            return http_response.json()
        else:
            return {}

    def add_user(self,username,firstname,surname,mail,password):
        """
            Inscrit un utilisateur sur le Core.

            Renvoie `True` si celui-ci à été ajouté `False` sinon
        """
        data = {
            'username':username,
            'first_name':firstname,
            'last_name':surname,
            'email':mail,
            'password':password,
            'tel':'none'
        }
        req = requests.post(self.urlCore+"/users/", data = data)
        if(req.status_code == 201):
            return True
        else:
            return False

    def login_user(self,username,password):
        """
            Vérifie si les identifiants fonctionnent avec le Core.

            Si les identifiants sont bon, renvoi un dictionnaire contenant les informations de l'utilisateur et le token d'identification.

            Sinon renvoie None

            Attention : Pour identifier un utilisateur dans une vue il faut utiliser la methode native de django: 

            >>> user = authenticate(username=username, password=password, request=request)
        """
        try:
            token = self.get_token(username,password)
            if token:
                req = self.requete_core_get("/users/"+username+"/",token)
                req['token'] = token
                return req
            else:
                return None
        except:
            return None
