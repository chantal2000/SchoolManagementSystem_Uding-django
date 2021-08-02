from django.db import models
import datetime
from datetime import datetime
from django_countries.fields import CountryField
# from languages.fields import LanguageField
from django.db.models.fields import PositiveBigIntegerField
from phonenumber_field.modelfields import PhoneNumberField
from django.conf.global_settings import LANGUAGES

# from djangotoolbox.fields import ListField


# Create your models here.
class Student(models.Model):
    first_name=models.CharField(max_length=12)
    last_name=models.CharField(max_length=12)
    country = CountryField()
    age=models.PositiveSmallIntegerField()
    date_of_birth = models.DateTimeField(default=datetime.now)
    languages = models.CharField(max_length=7, choices=LANGUAGES)

    Roll_number=models.CharField(max_length=5)
    student_id=models.PositiveSmallIntegerField()
    National_Id=models.CharField(max_length=16)
    CHOICES=(
        ('F',"Female"),
        ('M',"Male")
    )
  
    Gender=models.CharField(max_length=10,choices=CHOICES)
    phone_number=PhoneNumberField() 
    Guardian_name=models.CharField(max_length=40)
    Email_address=models.EmailField(max_length=30)
    Gender=models.CharField(max_length=10,choices=CHOICES)
    profile_image=models.ImageField()
    Grade=models.CharField(max_length=2)
    Medical_report=models.FileField(upload_to='uploads',blank=True)
    date_Of_enrollment=models.DateTimeField(default=datetime.now)
    course_name=models.CharField(max_length=30)
    laptop_number=models.CharField(max_length=7)
    # languages=models.CharField(max_length=10,choices=LANGUAGES)
    # languages=models.ManyToManyField()
    # languages = LanguageField()
    # Languages=models.ListField()
    # some_choices = models.ListField(LANGUAGES)

    # phone_number=models.Phone


    
   