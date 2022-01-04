from django.contrib import admin
from .models import Comment, Place, Post
# Register your models here.
admin.site.register(Post)
admin.site.register(Place)
admin.site.register(Comment)