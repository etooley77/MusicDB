from django.db import models

# Create your models here.
class LoginUser(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)

    def __str__(self):
        return(f'{ self.username }')