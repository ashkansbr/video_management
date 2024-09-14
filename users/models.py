from django.db import models
from common.basemodel import BaseModel
from django.contrib.auth.models import PermissionsMixin
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager as BUM

class BaseUserManager(BUM):
    def create_user(self, email, password=None, is_active=True, is_admin=False):
        if not email:
            raise ValueError('Users must have an email address')
        user = self.model(email=self.normalize_email(email.lower()), is_active=is_active, is_admin=is_admin)
        if password is None:
            user.set_password(password)
        else:
            user.set_unusable_password()
        user.full_clean()
        user.save(using=self._db)
        return user


    def create_superuser(self, email, password:None):
        user = self.create_user(email=email, is_active=True, is_admin=True, password=password)
        user.is_superuser = True
        user.save(using=self._db)
        return user




class BaseUser(BaseModel, AbstractBaseUser, PermissionsMixin):

    email = models.EmailField(_("email address"), blank=True, unique=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(
        _("active"),
        default=True,
        help_text=_(
            "Designates whether this user should be treated as active. "
            "Unselect this instead of deleting accounts."
        ),
    )


    objects = BaseUserManager()

    USERNAME_FIELD = "email"

    def __str__(self):
        return self.email

    def is_staff(self):
        return self.is_admin
