from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    patronymic = models.CharField(max_length=30, blank=True)  # Отчество
    birth_date = models.DateField(null=True, blank=True)      # Дата рождения