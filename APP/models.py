from django.db import models
from django.core.validators import RegexValidator

# Create your models here.

alphanuemrical = RegexValidator

class UserProfile(models.Model):
    name = models.CharField(max_length=200)
    username = models.CharField(max_length=300, validators=[RegexValidator(regex=r'^@[a-zA-Z0-9_]*$', message="Username can only contain letters, numbers, and underscores.", code='invalid_username')])
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100, validators=[RegexValidator(regex=r'^@[a-zA-Z0-9_]*$', message="Password can only contain letters, numbers, and underscores(@).", code='invalid_password')])
    image = models.ImageField(null=True, blank=True, upload_to='APP/static/users')