from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)
from simple_history.models import HistoricalRecords

# Create your models here.

class UserManager(BaseUserManager):
    def __create_user(self, username, email, name, is_staff, is_superuser, password):
        user = self.model(username=username, email=email, name=name, is_staff=is_staff, is_superuser=is_superuser)
        user.set_password(password)
        user.save(self.db)
        return user

    def create_user(self, username, email, name, password):
        return self.__create_user(username, email, name, False, False, password )
    
    def create_superuser(self, username, email, name, password):
        return self.__create_user(username, email, name, True, True, password )


class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField("Username", max_length=50, unique=True)
    email = models.EmailField("Email", max_length=254, unique=True)
    name = models.CharField("Name", max_length=50, blank=True, null=True)
    last_name = models.CharField("Last Name", max_length=50, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    objects = UserManager()
    historical = HistoricalRecords()

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["email", "name"]

    