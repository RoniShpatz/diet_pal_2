from django.db import models
from django.contrib.auth.models import User
from diet_log.models import Meals


class Post(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    meal = models.ForeignKey(Meals, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.title
