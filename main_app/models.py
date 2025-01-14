# Create your models here.
from django.db import models
from datetime import date

# A tuple of 2-tuples
Results = (
    ('W', 'Win'),
    ('L', 'Loss'),
    ('N', 'Not played')
)

# Create your models here.
class Baseball(models.Model):
    team_name = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    stadium = models.CharField(max_length=100)
    start_date = models.IntegerField()

    def __str__(self):
        return self.team_name
    
    def game_of_the_day(self):
        return self.games_set.filter(date=date.today()).count() >= len(Results)

# Add new Feeding model below Games model
class Games(models.Model):
    date = models.DateField("game date")
    result = models.CharField(
        max_length=1,
        choices=Results,
        # set the default value for results to be 'N' for Not played
        default=Results[0][0]
    )

     # Create a baseball_id FK
    Baseball = models.ForeignKey(Baseball, on_delete=models.CASCADE)

    def __str__(self):
    # Nice method for obtaining the friendly value of a Field.choice
        return f"{self.Baseball} on {self.date}"

class Meta:
    ordering = ['-date']




