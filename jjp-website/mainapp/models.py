from django.db import models

class ResearchPaper(models.Model):
    """Class for uploading research papers"""
    paper = models.FileField(upload_to='research/')
    title = models.TextField()
    authors = models.TextField()
    venue = models.TextField()
    date = models.DateField()

class Car(models.Model):
    name = models.TextField()
    image = models.ImageField(upload_to='cars/', default=None, null=True, blank=True)

class CarPhoto(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    photos = models.FileField(null=True, blank=True)
    