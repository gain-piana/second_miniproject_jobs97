from django.db import models

# Create your models here.
# class JobsTest(models.Model):
#     name = models.CharField(max_length=50)
#     address = models.CharField(max_length=50)
#     link = models.CharField(max_length=200)
#     lat = models.FloatField()
#     lng = models.FloatField()

class ReviewTest(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=200)
    link = models.CharField(max_length=200)
    lng = models.FloatField()
    lat = models.FloatField()
    total_star = models.FloatField()
    star = models.FloatField()
    summary = models.CharField(max_length=500)
    good = models.CharField(max_length=500)
    bad = models.CharField(max_length=500)