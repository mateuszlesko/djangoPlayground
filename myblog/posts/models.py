from django.db import models
from django.db.models.deletion import CASCADE
from django.utils import timezone

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=32)
    content = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(default = timezone.now)
    author = models.ForeignKey('auth.User',on_delete=models.CASCADE)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return f"{self.title}\n {self.content}"

