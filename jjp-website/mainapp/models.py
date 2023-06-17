from django.db import models

class ResearchPaper(models.Model):
    """Class for uploading research papers"""
    paper = models.FileField(upload_to='research/')
    title = models.TextField()
    authors = models.TextField()
    venue = models.TextField()
    date = models.DateField()
    