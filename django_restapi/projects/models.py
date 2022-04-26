from django.db import models


# Create your models here.
class Movie(models.Model):
    def __str__(self):
        return self.moviename
    image = models.ImageField(upload_to="images", default='images/none/sample.jpgp')
    moviename = models.CharField(max_length=100)
    description = models.CharField(max_length=200,null=True, blank=True)
    rating = models.FloatField()



