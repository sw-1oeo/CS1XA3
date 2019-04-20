from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    max_score = models.IntegerField()
    
    def __str__(self):
        return "{} {}".format(self.user.username,self.max_score)

