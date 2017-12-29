from django.db import models

# Create your models here.
class Plan(models.Model):
    name = models.CharField(max_length=200)
    cost = models.IntegerField(default=0)

    def __str__(self):
        return self.name

class User(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    password = models.CharField(max_length=255)
    plan = models.ForeignKey(Plan,on_delete=models.CASCADE)

    def __str__(self):
        return "%s %s" % (self.first_name,self.last_name)