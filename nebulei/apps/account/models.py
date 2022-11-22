from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser, PermissionsMixin, BaseUserManager
from django.utils.translation import gettext_lazy as _

from account.config import FIRST_NAME_MAX_LENGTH, LAST_NAME_MAX_LENGTH, \
    DISPLAY_NAME_MAX_LENGTH, USERNAME_MAX_LENGTH, \
    PASSWORD_MAX_LENGTH, BIO_MAX_LENGTH, PROWESS_MAX_SELECTION, \
    EMAIL_MAX_LENGTH

from account.username import default_display_name

from categories.prowess import PROWESS_SELECTION



class CustomUserManager(BaseUserManager):

    def create_user(self, email,username, password, **extra_fields):
        """
          Create and save a SuperUser with the given email,first name , lastname and password.
        """
        if not email:
            raise ValueError(_('The Email must be set'))
        if not username:
            raise ValueError(_('Username must be set'))
        if not password:
            raise ValueError(_('Password must be set'))

        email = self.normalize_email(email)
        user = self.model(email=email,username=username, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email,username, password, **extra_fields):
        """
        Create and save a SuperUser with the given email,first name , lastname and password.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True.'))
        return self.create_user(email,username, password, **extra_fields)


class User(AbstractUser):

    avatar = models.ImageField (
        upload_to="avatar",
        null=True, 
        blank=True,
    )

    first_name = models.CharField (
        max_length=FIRST_NAME_MAX_LENGTH,
    )

    last_name = models.CharField (
        max_length=LAST_NAME_MAX_LENGTH,
    )

    display_name = models.CharField (
        max_length=DISPLAY_NAME_MAX_LENGTH,
        blank=False,
        null=False,
        default=default_display_name,
    )

    username = models.CharField (
        _('username'),
        max_length=USERNAME_MAX_LENGTH,
        blank=False,
        null=False,
        unique=True,
    )

    email = models.EmailField (
        _('email address'),
        max_length=EMAIL_MAX_LENGTH,
        unique=True, 
        null=False, 
        blank=False,
    )

    password = models.CharField (
        max_length=PASSWORD_MAX_LENGTH,
        unique=True,
    )

    prowess = models.CharField (
        max_length=PROWESS_MAX_SELECTION,
        choices=PROWESS_SELECTION,
        default='',
    )

    bio = models.CharField (
        max_length=BIO_MAX_LENGTH,
        blank=True,
    )

    verified = models.BooleanField(default=False)

    updated_at = models.DateTimeField(auto_now=True)

    date_joined = models.DateTimeField(auto_now_add=True)


    USERNAME_FIELD = 'email'

    REQUIRED_FIELDS = ['username', 'password', 'first_name', 'last_name']


    def __str__(self):
        return self.username

