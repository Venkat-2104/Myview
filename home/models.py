from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class movie(models.Model):
    name = models.CharField(max_length=100)
    release_date = models.DateField()
    director = models.CharField(max_length=100,default='YourDefaultDirectorName')
    summary = models.TextField()
    image = models.ImageField(upload_to="poster")
    average_rating = models.DecimalField(max_digits=3, decimal_places=2, null=True, blank=True)

class review(models.Model):
    user = models.ForeignKey(User,on_delete=models.SET_NULL,null=True,blank=True)
    movie_name = models.CharField(max_length=100,default="defaultmoviename")
    _review = models.TextField(default="blank review")
    rating = models.DecimalField(max_digits=2, decimal_places=1)


