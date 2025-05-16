from django.db import models

# Create your models here.

class users(models.Model):
    uname=models.CharField(max_length=20)
    uemail=models.EmailField(max_length=50)
    upass=models.TextField(max_length=20)