from django.db import models
from django.contrib.auth.models import User

class ScoreBoard(models.Model):

    score = models.IntegerField()
    datetime = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self) -> str:
        return str(self.user)