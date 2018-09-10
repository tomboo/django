from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Weight(models.Model):
    date_posted = models.DateTimeField(default=timezone.now)
    weight = models.FloatField()
    bodyfat = models.FloatField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.date_posted}, {self.weight}, {self.bodyfat}, {self.author}'
