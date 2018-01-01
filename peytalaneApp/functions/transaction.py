class Transaction():
    
    def __init__(self,price,product,action_payment):
        self.price = price
        self.product = product
        self.action_payment = action_payment

    def payment(self):
        self.action_payment()

