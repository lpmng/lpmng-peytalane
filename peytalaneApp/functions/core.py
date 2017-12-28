import requests

class CoreRequest():
    urlCore = "http://127.0.0.1:8000"

    def addUser(self,username,firstname,surname,mail,password):
        data = {
            'uid':username,
            'commonname':firstname,
            'surname':surname,
            'mail':mail,
            'password':password,
            'tel':'none'
        }
        req = requests.post(self.urlCore+"/users/", data = data)
        print(req.status_code)
        print(req.text)
        if(req.status_code == 201):
            return True
        else:
            return False
