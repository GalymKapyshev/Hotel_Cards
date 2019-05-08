from django.db import models

# Create your models here.
class Clients(models.Model):
    name = models.CharField(max_length = 250)
    country = models.CharField(max_length = 250)
    birth = models.CharField(max_length = 250)
    passport = models.CharField(max_length = 250)
    issue = models.CharField(max_length = 250)
    expiry = models.CharField(max_length = 250)
    email = models.EmailField()
    music = models.CharField(max_length=250)
    file = models.CharField(max_length=250)

    def __str__(self):
        return self.name