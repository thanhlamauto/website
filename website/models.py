from django.db import models
from django.contrib.auth.models import AbstractUser
from ckeditor.fields import RichTextField

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(blank=True, max_length = 255)
    content = RichTextField(blank=True)
    photo = models.ImageField(upload_to='website/images/blogCover', blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    tag = models.CharField(max_length=225, blank=True, null=True)
    
    class Meta:
        ordering = ['-timestamp']
    
    def serialize(self):
        return {
            "id": self.id,
            "title": self.title,
            "content":self.content,
            "photo":self.photo,
            "timestamp": self.timestamp.strftime("%b %d %Y, %I:%M %p"),
            "tag":self.tag,
        }
    
class Book(models.Model):
    bookName = models.CharField(max_length=255)
    image = models.ImageField(upload_to='website/images/blogCover', blank=True, null=True)
    bookUrl = models.URLField(max_length=255)
    level = models.CharField(max_length=225, blank=True, null=True)