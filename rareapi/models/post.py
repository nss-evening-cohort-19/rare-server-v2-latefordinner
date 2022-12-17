from django.db import models

class Post(models.Model):

    user = models.ForeignKey("User", on_delete=models.CASCADE)
    category = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    publication_date = models.DateField()
    image_url = models.CharField(max_length=100)
    content = models.CharField(max_length=300)
    approved = models.BooleanField()
