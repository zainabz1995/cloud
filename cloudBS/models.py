from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
User = get_user_model()


class Station(models.Model):
    location_name = models.CharField(max_length=30)


class Board(models.Model):
    board_id = models.CharField(max_length=30)
    location = models.ForeignKey(Station, on_delete=models.CASCADE)
    energy = models.PositiveIntegerField()
    power = models.IntegerField()
    voltage = models.IntegerField()
    current = models.IntegerField()
    start_time_instant = models.DateTimeField()
    stop_time_instant = models.DateTimeField()


class Country(models.Model):
    name = models.CharField(max_length=30)


class City(models.Model):
    name = models.CharField(max_length=30)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    population = models.PositiveIntegerField()
