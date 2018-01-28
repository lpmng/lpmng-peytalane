
import os
import json
import requests

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


class CoreRequest():
    urlCore = "http://127.0.0.1:8001"

    def get_token(self,user,pwd):
        """
            recupere un token de l'api du core si le user et le mot de passe correspondent
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

    def requete_core_get(self,url_api,token):
        """
        fait une requete sur l'api du core et renvoi le résultat en json (le token doit être valide)
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

    def addUser(self,username,firstname,surname,mail,password):
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
    
    def logUser(self,username,password):
        try:
            token = self.get_token(username,password)
            if token:
                print('test')
                req = self.requete_core_get("/users/"+username+"/",token)
                req['token'] = token
                return req
            else:
                return {}
        except:
            return {}
