from django.db import models
from django.utils import timezone
from users.managers import CustomUserManager
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin

class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(verbose_name="Адрес email", unique=True)
    is_active = models.BooleanField(default=True, verbose_name="Активный пользователь")
    is_staff = models.BooleanField(default=False, verbose_name="Статус персонала")
    date_join = models.DateTimeField(default=timezone.now)
    
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS =[]
    
    objects = CustomUserManager()
    
    def __str__(self) -> str:
        return self.email
