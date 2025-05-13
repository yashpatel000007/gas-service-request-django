from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    is_customer = models.BooleanField(default=True)
    is_support = models.BooleanField(default=False)

