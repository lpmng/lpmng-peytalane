from peytalaneApp.models_dir.user import User
from peytalaneApp.models_dir.tournament import *


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
