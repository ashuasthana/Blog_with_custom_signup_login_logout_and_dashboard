from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    title=models.CharField(max_length=150)
    desc=models.TextField()
    author=models.ForeignKey(User,on_delete=models.CASCADE,related_name='blog_posts',default=3)
