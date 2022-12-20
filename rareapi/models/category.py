from django.db import models

class Category(models.Model):
    """Database category model"""
    label = models.CharField(max_length=50)
