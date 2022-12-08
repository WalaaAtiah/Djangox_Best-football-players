from django.db import models
from accounts.models import CustomUser
from django.urls import reverse

class Player (models.Model):
    name  = models.CharField(max_length=255, help_text="name", default="Name")
    team  = models.CharField(max_length=255, help_text="team name", default="Team")
    Position  = models.CharField(max_length=255, help_text="Position", default="Position")
    Age=models.IntegerField()
    publisher = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    data = models.TextField(default="information ")
    image = models.TextField(default= "add the path of picture")
   
    def __str__(self):
       return self.name
    class Meta:
       verbose_name_plural = "players"   
       ordering=['pk']

    def get_absolute_url(self):
        return reverse('player_detail',args=[self.id])

    