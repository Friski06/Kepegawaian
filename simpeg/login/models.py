from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission

from django.utils.translation import gettext_lazy as _
from .managers import CustomUserManager


class User(AbstractUser):
    USER_TYPE_CHOICES = (
        ('admin', 'Admin'),
        ('kaunit', 'Ka.Unit'),
        ('staf', 'Staf'),
    )
    user_type = models.CharField(max_length=10, choices=USER_TYPE_CHOICES, blank=True)
    username = None
    email = models.EmailField(_("email address"), unique=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email
    
    groups = models.ManyToManyField(Group, related_name='login_users', blank=True)
    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name='user permissions',
        related_name='login_users',
        blank=True,
        help_text='Specific permissions for this user.',
        related_query_name='login_user',
    )