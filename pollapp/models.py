from django.db import models

# Create your models here.
class Question(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choices = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return "{} votes for {}".format(self.votes,self.choices)