
from django.db import models
from django.urls import reverse  # To generate URLS by reversing URL patterns
from django.db.models import UniqueConstraint
from django.db.models.functions import Lower
from django.contrib.auth.models import User

class Water(models.Model):
    id = models.AutoField(primary_key=True)
    mil = models.IntegerField()  #numbers represent milliliters
    date = models.DateField()
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.mil} ml on {self.date}"

class Wieght(models.Model):
    id = models.AutoField(primary_key=True)
    amount = models.IntegerField()
    date = date = models.DateField()
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.amount} kg"
    
class Workout(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)  
    duration = models.IntegerField()  
    date = models.DateField()
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} for {self.duration} minutes"
    

class Meals(models.Model):
    id = models.AutoField(primary_key=True)
    content = models.CharField(max_length=200)
    date = models.DateField()
    time = models.TimeField()
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.time.strftime('%H:%M')} : {self.content}"
    
class FavMeals(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20) 
    content = models.CharField(max_length=200)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.content} for user {self.user_id}" 