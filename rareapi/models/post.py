from django.db import models

class Post(models.Model):

    user_id = models.CharField(max_length=50)
    category_id = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    publication_date = models.DateField()
    image_url = models.CharField(max_length=100)
    content = models.CharField(max_length=300)
    approved = models.BooleanField()
