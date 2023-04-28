from django.db import models
from django.core.exceptions import ValidationError

# Create your models here.
class Post(models.Model):
    Male = 'M'
    FeMale = 'F'
    GENDER_CHOICES = (
    (Male, 'Male'),
    (FeMale, 'Female'),
    )

    first_name = models.CharField(max_length=22 )
    last_name = models.CharField(max_length=22 )
    date_of_birth = models.DateTimeField(null=True, blank=True)
    gender = models.CharField(max_length=22, choices = GENDER_CHOICES, default = Male )
    country = models.CharField(max_length=22 )
    state = models.CharField(max_length=22 )
    town = models.CharField(max_length=22 )
    zipcode = models.IntegerField(default =0)
    phonenumber1 = models.IntegerField(default =0)
    phonenumber2 =models.IntegerField(default =0)
    email = models.CharField(max_length=30 )

    def clean_my_field(self):
        if not self.first_name:
            raise ValidationError('my_field cannot be empty')