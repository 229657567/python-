from django.db import models

# Create your models here.
class phone(models.Model):
    title=models.CharField(max_length=255)
    price=models.CharField(max_length=255)

class movie(models.Model):
    title=models.CharField(max_length=255)    
