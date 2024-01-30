from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.db.models.signals import pre_save
from Forum.utils import unique_slug_generator


# Create your models here.
class institute(models.Model):
       id = models.AutoField(primary_key=True)
       name = models.CharField(max_length=100)
       link = models.URLField(max_length=100)
       
class questions(models.Model):
       id = models.AutoField(primary_key=True)
       TiTLe = models.CharField(max_length=100)
       slug = models.SlugField(max_length=250, null=True , blank= True)
       user = models.ForeignKey(User,on_delete=models.CASCADE)
       Tag = models.CharField(max_length=100)
       Content = models.TextField(max_length=100)
       created = models.DateTimeField(auto_now_add=True)
       updated = models.DateTimeField(auto_now=True)   
                 
       def __str__(self):
          return self.TiTLe 
def slug_generator(sender, instance, *args ,**kwargs):    
    if not instance.slug:          
      instance.slug =  unique_slug_generator(instance)

pre_save.connect(slug_generator,sender=questions)
          
          
          
          
          
          
          
          
          
          
          
          
class Comment(models.Model):
    id = models.AutoField(primary_key=True)
    post = models.ForeignKey(questions, related_name= 'comments',on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    content= models.TextField(max_length=100)
    timestamp = models.TimeField(auto_now_add=True)
    
    def __str__(self):
        return self.post.TiTLe
    
    

      