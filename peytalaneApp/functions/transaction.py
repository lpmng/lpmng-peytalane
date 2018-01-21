class Transaction():
    
    def __init__(self,price,product,action_payment,args):
        self.price = price
        self.product = product
        self.action_payment = action_payment
        self.args = args

    def payment(self):
        if self.action_payment == "lan":
            callback_lan(self.args)
        elif self.action_payment == "tournoi":
            self.callback_payment(self.args)

    def callback_payment(self,args):
        print("toto - callback")

    def callback_lan(self,args):
        user = User.objects.get(username = args["user"])
        user.lan = True