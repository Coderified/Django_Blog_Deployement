from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=50)

class Post(models.Model):
    title=models.CharField(max_length=50)
    body=models.TextField()
    createdon = models.DateTimeField(auto_now_add=True)
    modifiedon = models.DateTimeField(auto_now=True)
    categories = models.ManyToManyField("Category",related_name='posts')
