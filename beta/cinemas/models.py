from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

class Cinema(models.Model):
    name = models.CharField(max_length=100)
    seats=models.PositiveSmallIntegerField()


    def __str__(self):
        return f" {self.name} liczba miejsc: {self.seats}"


class Movie(models.Model):
    title = models.CharField(max_length=100)
    minimum_age = models.PositiveSmallIntegerField()

    def __str__(self):
        return f" {self.title} minimalny wiek: {self.minimum_age}"


class Projection(models.Model):
    cinema=models.ForeignKey(Cinema, on_delete=models.CASCADE)
    movie=models.ForeignKey(Movie, on_delete=models.CASCADE)
    date=models.DateTimeField()
    publiszed=models.BooleanField()
    tickets_availble=models.PositiveSmallIntegerField()

    def __str__(self):
        return f"{self.movie.title} at {self.cinema.name} on {self.date.strftime('%d.%m.%y %H:%M')}"
