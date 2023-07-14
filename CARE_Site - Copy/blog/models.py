from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=50)

class Post(models.Model):
    title=models.CharField(max_length=50)
    body=models.TextField(blank=True,null=True)
    sitelink=models.URLField(max_length=200,blank=True,null=True)
    file=models.FileField(upload_to='files/',blank=True,null=True,default=None)
    createdon = models.DateTimeField(auto_now_add=True)
    modifiedon = models.DateTimeField(auto_now=True)
    categories = models.ManyToManyField("Category",related_name='posts')

    class Meta:
        ordering = ['modifiedon']

    def __str__(self):
        return f"{self.title}"