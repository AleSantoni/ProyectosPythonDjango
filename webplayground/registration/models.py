
from django.conf import settings
from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.urls import URLPattern
from django.db.models.signals import post_save




# Create your models here.
def custom_upload_to(instance, filename):
    old_instance = Profile.objects.get(pk=instance.pk)
    old_instance.avatar.delete()
    return 'profiles/' + filename


class Profile(models.Model):
    user= models.OneToOneField(User, on_delete=models.CASCADE)
    avatar= models.ImageField(upload_to= custom_upload_to, blank=True, null=True)
    bio= models.TextField(blank=True, null=True)
    link= models.URLField(max_length=200, blank=True, null=True)  
    
    
    class Meta:
        ordering = ['user__username']

    def __str__(self):
        return self.user.username
    
@receiver(post_save, sender=User)
def ensure_profile_exists(sender,instance, **kwargs):
    Profile.objects.get_or_create(user=instance)
   
   