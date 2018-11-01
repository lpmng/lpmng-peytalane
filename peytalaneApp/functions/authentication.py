from peytalaneApp.models_dir.user import User
from peytalaneApp.functions.core import CoreRequest

class CoreBackend(object):
    """ 
        Module qui gère l'authentification

        Permet l'appel au fonctions d'authentification natives de django:
        * ` django.contrib.auth.auhentificate ` qui vérifie si un couple username/password est valide
        * ` django.contrib.auth.login ` qui enregistre la connexion de l'utilisateur en session
        * et d'autre voir https://docs.djangoproject.com/fr/1.11/topics/auth/default/

        Permet aussi à ce que la connexion soit uniforme sur le site web et sur la page admin

    """
    def authenticate(self, request, username=None, password=None):
        """
            Authentifie un couple username/password.

            Ne pas utiliser directement mais via le wrapper django:

            - ` django.contrib.auth.auhentificate `
        """
        core = CoreRequest()
        user = core.login_user(username,password)

        if user is not None:
            request.session['token'] = user['token']
            #request.session['username'] = username
            request.session['transactions'] = dict()
            request.session["transactions_max_id"] = 0
            obj, created  = User.objects.get_or_create(username=username)
            request.user = obj
            return obj
        return None

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None

    def has_perm(self, user_obj, perm, obj=None):
        return user_obj.admin