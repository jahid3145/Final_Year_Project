from django.db import models

# Create your models here.
from django.db.models import CASCADE


class ClientRegister_Model(models.Model):

    username = models.CharField(max_length=30, default="unknown")
    email = models.EmailField(max_length=30, default="unknown")
    password = models.CharField(max_length=10, default="unknown")
    phoneno = models.CharField(max_length=10, default="unknown")
    country = models.CharField(max_length=30, default="unknown")
    state = models.CharField(max_length=30, default="unknown")
    city = models.CharField(max_length=30, default="unknown")
    gender= models.CharField(max_length=30, default="unknown")
    address= models.CharField(max_length=30, default="unknown")


class predict_investor_sentiment(models.Model):

    Investor_Age= models.CharField(max_length=300, default="unknown")
    Investor_Gender= models.CharField(max_length=300, default="unknown")
    PDate= models.CharField(max_length=300, default="unknown")
    Stock_Text= models.CharField(max_length=30000, default="unknown")
    Stock_Name= models.CharField(max_length=300, default="unknown")
    Company_Name= models.CharField(max_length=300, default="unknown")
    Prediction= models.CharField(max_length=300, default="unknown")


class detection_accuracy(models.Model):

    names = models.CharField(max_length=300, default="unknown")
    ratio = models.CharField(max_length=300, default="unknown")

class detection_ratio(models.Model):

    names = models.CharField(max_length=300, default="unknown")
    ratio = models.CharField(max_length=300, default="unknown")



