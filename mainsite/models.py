from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class LoginUser(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)

    def __str__(self):
        return(f'{ self.username }')
    
class Artist(models.Model):
    class Months(models.TextChoices):
        JAN = 'January'
        FEB = 'February'
        MAR = 'March'
        APR = 'April'
        MAY = 'May'
        JUN = 'June'
        JUL = 'July'
        AUG = 'August'
        SEP = 'September'
        OCT = 'October'
        NOV = 'November'
        DEC = 'December'

    artist_name = models.CharField(max_length=100)
    real_name = models.CharField(max_length=100)
    bands = models.CharField(max_length=200)
    birth_year = models.IntegerField(max_length=4)
    birth_month = models.CharField(max_length=12, choices=Months.choices, default=Months.JAN)
    birth_day = models.IntegerField(max_length=2)
    death_year = models.IntegerField(max_length=4, blank=True, null=True)
    death_month = models.CharField(max_length=12, choices=Months.choices, default=None, blank=True, null=True)
    death_day = models.IntegerField(max_length=2, blank=True, null=True)
    about_section = models.TextField(max_length=10000)

    added_by = models.ForeignKey(User, on_delete=models.CASCADE)
    added_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.artist_name