from django.db import models

class Scholarship(models.Model):
    title = models.CharField(max_length=200)
    provider = models.CharField(max_length=200)
    amount = models.IntegerField()
    deadline = models.DateField()
    description = models.TextField()

    def __str__(self):
        return self.title
