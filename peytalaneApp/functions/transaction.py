from peytalaneApp.models_dir.user import User
from peytalaneApp.models_dir.tournament import *
from peytalaneApp.models_dir.food import *
from peytalaneApp.models_dir.payment import *
import requests
import json
import pdb
import requests

class Transaction():

    def __init__(self,price,product,action_payment,args,comment):
        self.price = price
        self.product = product
        self.action_payment = action_payment
        self.args = args
        self.comment = comment


    @staticmethod
    def new_transaction(request,price,product,action_payment,args,comment=""):
        if not "transactions_max_id" in request.session:
            request.session["transactions_max_id"] = 0
            request.session["transactions"] = dict()
            request.session.modified = True
        
        transaction = {
            "price":price,
            "product":product,
            "action_payment":action_payment,
            "args":args,
            "comment":comment
        }
        request.session["transactions"][request.session["transactions_max_id"] + 1] = transaction
        request.session["transactions_max_id"] = request.session["transactions_max_id"]+1
        request.session.modified = True

    @staticmethod
    def clean_transaction(request,action_payment):
        keys = request.session["transactions"].keys()
        new_dict = dict()
        for key in keys:
            transaction = request.session["transactions"][key]
            #pdb.set_trace()
            
            if transaction["action_payment"] != action_payment:
                new_dict[key] = request.session["transactions"][key]

        request.session["transactions"] = new_dict
        request.session.modified = True


    @staticmethod
    def delete_transaction(request,id):
        request.session["transactions"].pop(id)
        request.session.modified = True


    def payment(self):
        if self.action_payment == "lan":
            self.callback_lan(self.args)
        elif self.action_payment == "tournament":
            self.callback_tournament(self.args)
        elif self.action_payment == "food":
            self.callback_food(self.args)


    def callback_tournament(self,args):
        #parses args
        user = User.objects.get(username = args["user"])
        tournament = Tournament.objects.get(id = args["id_tournament"])
        pseudo = args["pseudo"]
        #save infos in bdd
        participant = Participant()
        participant.game_pseudo = pseudo
        participant.user = user
        participant.save()
        tournament.participants.add(participant)
        #save transaction
        self.save_transaction(tournament.name,user)


    def callback_lan(self,args):
        user = User.objects.get(username = args["user"])
        user.lan = True
        user.save()
        # TODO rajouter une session dans lpmng
        self.save_transaction("lan",user)



    def callback_food(self,args):
        user = User.objects.get(username = args["user"])
        food = Food.objects.get(id = args["id_food"])
        self.save_transaction(food.name,user,args["options"])
        

    def save_transaction(self,product,user,options=dict()):
        #save transaction
        payment = Payment()
        payment.price = self.price
        payment.type_product = self.action_payment
        payment.product = product
        payment.user = user
        payment.comment = self.comment
        payment.save()

        for options_key in options.keys():
            po = Payment_option.objects.get_or_create(name=options_key)
            pv = Payment_option_value(
                value = options[options_key][1],
                option = po[0],
                payment = payment
            )
            pv.save()


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
