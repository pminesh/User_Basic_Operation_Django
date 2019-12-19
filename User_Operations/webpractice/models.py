from django.db import models
from django.contrib.auth.models import User

#user profile model

class UserProfile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    description = models.CharField(max_length=100,default='')
    url = models.URLField(default='')
    phone  =  models.IntegerField(default=0)
    image  = models.ImageField(upload_to='profile_image',blank=True)
    
    def __str__(self):
        return self.user.username #return user name