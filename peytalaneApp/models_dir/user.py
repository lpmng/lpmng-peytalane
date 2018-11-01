from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)
from peytalaneApp.functions.core import CoreRequest

class CoreUserManager(BaseUserManager):
    def create_user(self, username, password):
        """
        Creates a user if this one exists in the core and password match with username
        """
        core = CoreRequest()
        user = core.login_user(username,password)

        if user is None:
            raise ValueError('This user does not exist in the core') 

        user, created  = User.objects.get_or_create(username=username)
        user.save(using=self._db)

        return user

    def create_superuser(self, username, password):
        """
        Creates and saves a superuser
        """
        user = self.create_user(username,password)
        user.admin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    username = models.CharField(max_length=100,unique =True)
    lan = models.BooleanField(default=False)
    admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    objects = CoreUserManager()
    
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []
    
    @property
    def is_authenticated(self):
        return True

    @property
    def is_staff(self):
        return self.admin

    @property
    def is_superuser(self):
        return self.admin

    def get_full_name(self):
        return self.username

    def get_short_name(self):
        return self.username

    def __str__(self):
        return self.username
    
    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True


