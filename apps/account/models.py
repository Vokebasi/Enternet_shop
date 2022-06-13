from django.db import models
from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser
from django.core.mail import send_mail

# моделька юзера
class User(AbstractBaseUser):
    email = models.EmailField(primary_key=True)
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    first_name = models.CharField(max_length=80, blank=True)
    last_name = models.CharField(max_length=70, blank=True)
    activation_code = models.CharField(max_length=8, blank=True)

    def __str__(self):
        return f'{self.email}'