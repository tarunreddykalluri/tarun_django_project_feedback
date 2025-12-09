from django.db import models

class Feedback(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    movie = models.CharField(max_length=100)
    email = models.EmailField()
    feed = models.TextField()

    def __str__(self):
        return f"{self.name} ({self.movie})"
