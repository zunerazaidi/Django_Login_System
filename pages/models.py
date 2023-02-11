from django.contrib.auth.models import (
    AbstractBaseUser
)
from django.db import models
from phone_field import PhoneField

from pages.manager import MyUserManager


class MyUser(AbstractBaseUser):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    date_of_birth = models.DateField()
    ROLE=(('User', "Regular - Can't delete members"), ('Admin', "Admin - Can delete members"))
    telephone = PhoneField(blank=True)
    role = models.CharField(max_length=20, choices=ROLE, default='User', )
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = MyUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'date_of_birth', 'role']

    def __str__(self):
        return self.email

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin
