# Create your models here.
from django.db import models

# Create your models here.
class Baseball(models.Model):
    team_name = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    stadium = models.CharField(max_length=100)
    start_date = models.IntegerField()

    def __str__(self):
        return self.team_name
