from django.contrib.auth.base_user import BaseUserManager
from .utils import generate_confirmation_code


class UserManager(BaseUserManager):
    use_in_migrations = True

    # creating user
    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')

        email = self.normalize_email(email)
        # a user is created and stored in the db
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        # creating token for verification email address
        from users_app.models import VerifyEmailToken
        VerifyEmailToken.objects.create(email=user, token=generate_confirmation_code())
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email=email, password=password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_verified', True)
        return self._create_user(email=email, password=password, **extra_fields)