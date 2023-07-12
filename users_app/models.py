from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin, Group, Permission
from django.db import models
from users_app.managers import UserManager


# PermissionsMixin need to correct work of is_superuser
class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    date_joined = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_verified = models.BooleanField(default=False)
    groups = models.ManyToManyField(Group, related_name='user_set_user', blank=True)
    user_permissions = models.ManyToManyField(Permission, related_name='user_set_user', blank=True)

    objects = UserManager()

    # the name of the field on the User model that is used as the unique identifier
    USERNAME_FIELD = 'email'
    # list of the field names that will be prompted for when creating a user with the createsuperuser
    REQUIRED_FIELDS = ['first_name']

    def get_full_name(self):
        full_name = f'{self.first_name} {self.last_name}'
        return full_name

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'


class VerifyEmailToken(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    token = models.CharField()
