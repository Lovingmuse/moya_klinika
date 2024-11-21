from django.db import models

# Create your models here.
class Client(models.Model):
  name = models.CharField(max_length=255)
  animal = models.CharField(max_length=255)
  phone = models.IntegerField(null=True)
  joined_date = models.DateField(null=True)

def __str__(self):
    return f"{self.name} {self.animal}"