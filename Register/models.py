from django.db import models

class CustomUser(models.Model):
    Name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254, unique=True)
    Mobile = models.BigIntegerField(null=True)
    password = models.CharField(max_length=50)
    Re_Enter_password = models.CharField(max_length=50)
