from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models

# Added PermissionsMixin to be able to work with administration
from elsi_belsi_handmade.elsi_belsi_auth.managers import ElsiBelsiHandmadeUserManager


class ElsiBelsiHandmadeUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(
        unique=True,
    )

    is_staff = models.BooleanField(
        default=False,
    )

    is_superuser = models.BooleanField(
        default=False,
    )

    date_joined = models.DateTimeField(
        auto_now_add=True,
    )

    USERNAME_FIELD = 'email'

    objects = ElsiBelsiHandmadeUserManager()
