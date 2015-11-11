from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserProfile(models.Model):
    user = models.OneToOneField(User,related_name='user')
    image = models.FileField(upload_to="/image" , blank=True)
    
    def __str__(self, ):
        return self.user.first_name
    