from django.db import models
from django.contrib.auth.models import User
from django.db.models.base import Model
from django.db.models.deletion import CASCADE
from django.db.models.fields import EmailField
from django.utils import timezone

# Create your models here.

class Student(models.Model):
    
    GENDERS = (
        ('male', 'Male'),
        ('female', 'Female'),
    )
    
    LEVELS = (
        (1, 'Grade 1'),
        (2, 'Grade 2'),
        (3, 'Grade 3'),
        (4, 'Grade 4'),
        (5, 'Grade 5'),
        (6, 'Grade 6'),
        (7, 'Grade 7'),
        (8, 'Grade 8'),
        (9, 'Grade 9'),
        (10, 'Grade 10'),
        (11, 'Grade 11'),
        (12, 'Grade 12'),
    )
    
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    birthday = models.DateField(default=timezone.now)
    gender = models.CharField(max_length=10, choices=GENDERS)
    level = models.PositiveSmallIntegerField(choices=LEVELS)
    father = models.CharField(max_length=40, null=True, blank=True)
    mother = models.CharField(max_length=40, null=True, blank=True)
    phone = models.CharField(max_length=15)
    vaccine = models.BooleanField(verbose_name='Vaccinated?')
    vaccine_date = models.DateTimeField(default=timezone.now)

class Teacher(models.Model):
    
    GENDERS = (
        ('male', 'Male'),
        ('female', 'Female'),
    )

    user = models.OneToOneField(User, on_delete=CASCADE)
    birthday = models.DateField(default=timezone.now)
    gender = models.CharField(max_length=10, choices=GENDERS)
    phone = models.CharField(max_length=15)
    vaccine = models.BooleanField(verbose_name='Vaccinated?')
    vaccine_date = models.DateTimeField(default=timezone.now)

class School(models.Model):
    id = models.PositiveSmallIntegerField(primary_key=True)
    name = models.CharField(max_length=60)
    principal = models.CharField(max_length=40)
    address = models.TextField(max_length=100)
    phone = models.CharField(max_length=15)
    email = models.EmailField()

class Schedule(models.Model):
    schedule = models.DateTimeField(default=timezone.now)

class Admin(models.Model):
    email = models.EmailField()
    full_name = models.CharField(max_length=40)
    password = models.CharField(max_length=256)
