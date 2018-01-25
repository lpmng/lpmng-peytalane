from django.http import HttpResponseRedirect
from django.urls import reverse

def IsLogin(function):
    def wrap(self,request, *args, **kwargs):
        if('username' in request.session):
            return function(self,request, *args, **kwargs)
        else:
            return HttpResponseRedirect(reverse('login'))
    wrap.__doc__ = function.__doc__
    wrap.__name__ = function.__name__
    return wrap