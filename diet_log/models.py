
from django.db import models
from django.urls import reverse  # To generate URLS by reversing URL patterns
from django.db.models import UniqueConstraint
from django.db.models.functions import Lower
from django.contrib.auth.models import User
from cloudinary_storage.storage import MediaCloudinaryStorage


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
        return f"{self.amount}"
    
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
    file = models.ImageField(storage=MediaCloudinaryStorage(), null=True, blank=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        # Return a meaningful string representation of the model
        return f"{self.time.strftime('%H:%M')} : {self.content} (File: {self.file.name or 'Unnamed file'})"
    
class FavMeals(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20) 
    content = models.CharField(max_length=200)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.content} for user {self.user_id}" 
    

class UploadedFile(models.Model):
    id = models.AutoField(primary_key=True)
    file = models.ImageField(storage=MediaCloudinaryStorage())
    uploaded_at = models.DateTimeField(auto_now_add=True)
    user_id = models.ForeignKey(
    User, on_delete=models.CASCADE, 
    null=True,  
    blank=True  
)

    def __str__(self):
        return self.file.name or 'Unnamed file'
        


class Message(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sent_messages')
    recipient = models.ForeignKey(User, on_delete=models.CASCADE, related_name='received_messages')
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    def __str__(self):
        return f"Message from {self.sender.username} to {self.recipient.username}"


