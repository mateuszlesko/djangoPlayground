from django.db import models
from django.db.models.deletion import CASCADE
from django.utils import timezone

# Create your models here.

class Place(models.Model):
    town = models.CharField(max_length=32)

    def __str__(self):
        return f"{self.town}"

class Post(models.Model):
    title = models.CharField(max_length=32)
    content = models.TextField()
    address = models.CharField(max_length=64)
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(default = timezone.now)
    author = models.ForeignKey('auth.User',on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/', blank=True, default="default.png")
    place = models.ForeignKey(Place, on_delete= models.CASCADE,verbose_name="place where it is")
    
    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return f"{self.title}\n {self.content}"


class Comment(models.Model):
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey('auth.User',on_delete=models.CASCADE)
    post = models.ForeignKey(Post,on_delete=models.CASCADE)