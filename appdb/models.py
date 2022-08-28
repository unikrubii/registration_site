from django.db import models
from django.core.validators import MinLengthValidator


# Create your models here.
# class Gender(models.Model):
#     """
#     Gender
#     """
#     gender = models.CharField(max_length=42, unique=True)

#     def __str__(self):
#         return self.gender


# class Subscription(models.Model):
#     """
#     Subscription type of users
#     """
#     type = models.CharField(max_length=10, unique=True)

#     def __str__(self):
#         return self.type


class Account(models.Model):
    """
    User model
    """
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    email = models.EmailField(max_length=50, unique=True, blank=True, null=True)
    firstname = models.CharField(max_length=50, blank=True, null=True)
    lastname = models.CharField(max_length=50, blank=True, null=True)
    tel_number = models.CharField(max_length=10, validators=[MinLengthValidator(10)], blank=True, null=True)

    def __str__(self):
        return self.username
