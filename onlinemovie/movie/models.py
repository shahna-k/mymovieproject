from django.db import models

# Create your models here.

class Movies(models.Model):
    title=models.CharField(max_length=30)
    lang=models.CharField(max_length=20)
    year=models.IntegerField()
    image=models.ImageField(upload_to="movie/image",null=True,blank=True)

def __str__(self):
    return self.title