from peytalaneApp.models_dir.user import User
from peytalaneApp.models_dir.tournament import *
from peytalaneApp.models_dir.food import *
import requests
import json

import requests

class Transaction():

    def __init__(self,price,product,action_payment,args):
        self.price = price
        self.product = product
        self.action_payment = action_payment
        self.args = args

    def payment(self):
        if self.action_payment == "lan":
            self.callback_lan(self.args)
        elif self.action_payment == "tournament":
            self.callback_tournament(self.args)

    def callback_tournament(self,args):
        #parses args
        user = User.objects.get(username = args["user"])
        tournament = Tournament.objects.get(id = args["id_tournament"])
        pseudo = args["pseudo"]
        #save infos in bdd
        participant = Participant()
        participant.game_pseudo = pseudo
        participant.username = user.username
        tournament.participant.add(participant)

    def callback_lan(self,args):
        user = User.objects.get(username = args["user"])
        user.lan = True

    def callback_food(self,args):
        user = User.objects.get(username = args["user"])
        food = Food.objects.get(name = args["food"])
        foodBuy = FoodBuy()
        foodBuy.user = user
        foodBuy.food = food
        foodBuy.save()

    def lydia(self, amount, recipient):
        data = {
            'amount': str(amount),
            'currency': 'EUR',
            'type': 'phone',
            'recipient': recipient,
            'vendor_token': '5a6e0ccc06ee9066892222'
        }
        req = requests.post("https://homologation.lydia-app.com/api/request/do.json", data = data)
        if(req.status_code == 200):
            print(req.json())
            prout = req.json()
            return prout
        else:
            return False
