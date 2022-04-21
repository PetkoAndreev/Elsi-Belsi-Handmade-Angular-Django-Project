from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.core.validators import MaxValueValidator
from django.db import models
from rest_framework_simplejwt.tokens import RefreshToken
from .managers import ElsiBelsiHandmadeUserManager

# Added PermissionsMixin to be able to work with administration
AUTH_PROVIDERS = {'facebook': 'facebook', 'google': 'google', 'email': 'email'}


class ElsiBelsiHandmadeUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(
        unique=True,
    )

    confirm_password = models.CharField(
        max_length=1000,
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

    auth_provider = models.CharField(
        max_length=255, blank=False,
        null=False, default=AUTH_PROVIDERS['email'])

    USERNAME_FIELD = 'email'

    objects = ElsiBelsiHandmadeUserManager()

    # str method visualize data in admin panel as row, not as columns
    def __str__(self):
        return f'{self.email}'

    def tokens(self):
        refresh = RefreshToken.for_user(self)
        return {
            'refresh': str(refresh),
            'access': str(refresh.access_token)
        }


class Profile(models.Model):
    first_name = models.CharField(
        max_length=25,
        blank=True,
        null=True,
    )
    last_name = models.CharField(
        max_length=25,
        blank=True,
        null=True,
    )
    age = models.PositiveIntegerField(
        blank=True,
        null=True,
        validators=[
            MaxValueValidator(100),
        ],
    )
    profile_image = models.ImageField(
        upload_to='profiles',
        default='default_profile_image.jpg',
        blank=True,
        max_length=None,
    )

    facebook_url = models.URLField(
        blank=True,
        null=True,
    )
    linked_in_url = models.URLField(
        blank=True,
        null=True,
    )
    github_url = models.URLField(
        blank=True,
        null=True,
    )

    user = models.OneToOneField(
        ElsiBelsiHandmadeUser,
        on_delete=models.CASCADE,
        primary_key=True,
        blank=False,
        null=False,
    )

    @property
    def full_name(self):
        return "%s %s" % (self.first_name, self.last_name)

    # str method visualize data in admin panel as row, not as columns
    def __str__(self):
        return f'{self.full_name}'


# Good to be here, because of the administration, not in the urls
from .signals import *
