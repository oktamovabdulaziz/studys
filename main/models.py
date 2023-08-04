from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    name = models.CharField(max_length=255)


class Gender(models.Model):
    gender = models.CharField(max_length=255)

    def __str__(self):
        return self.gender


class Subject(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Teacher(models.Model):
    gender = models.ForeignKey(Gender, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    activ = models.BooleanField(default=False)
    money = models.IntegerField()

    def __str__(self):
        return self.name


class Student(models.Model):
    gender = models.ForeignKey(Gender, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    activ = models.BooleanField(default=False)
    price = models.IntegerField(default=0)

    def __str__(self):
        return self.name


class Registration(models.Model):
    gender = models.ForeignKey(Gender, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    age = models.IntegerField()
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    register = models.BooleanField(default=False)





