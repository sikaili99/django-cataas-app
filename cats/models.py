from django.db import models


class Cats(models.Model):
    name = models.CharField(max_length=250)
    age = models.IntegerField()
    image_url = models.CharField(max_length=2083)


class People(models.Model):
    name = models.CharField(max_length=250)
    age = models.IntegerField()


class Offer(models.Model):
    code = models.CharField(max_length=200)
    description = models.CharField(max_length=250)
    discount = models.FloatField()


