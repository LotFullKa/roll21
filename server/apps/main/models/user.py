from django.contrib.auth.base_user import AbstractBaseUser
from django.db import models

from main.managers import UserManager


class User(AbstractBaseUser):
    username = models.CharField(max_length=60, unique=True)

    USERNAME_FIELD = "username"

    objects = UserManager()

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = "users"
