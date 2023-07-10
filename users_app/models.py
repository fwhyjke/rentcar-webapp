from django.contrib.auth.base_user import AbstractBaseUser
from django.db import models
from .managers import UserManager


class User(AbstractBaseUser):
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    date_joined = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_verified = models.BooleanField(default=False)

    objects = UserManager()

    # the name of the field on the User model that is used as the unique identifier
    USERNAME_FIELD = 'email'
    # list of the field names that will be prompted for when creating a user with the createsuperuser
    REQUIRED_FIELDS = ['first_name']

    def get_full_name(self):
        full_name = f'{self.first_name} {self.last_name}'
        return full_name

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'
