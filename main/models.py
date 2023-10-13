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
    group_count = models.IntegerField(default=0)

    def __str__(self):
        return self.name


class Group(models.Model):
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    student_count = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        q = Group.objects.filter(teacher=self.teacher)
        if q.count() < self.teacher.group_count and q.count() != self.teacher.group_count:
            return super().save(*args, **kwargs)
        else:
            raise SystemError(f"Group qo'shish chegaralangan! maksimum {self.teacher.group_count}!")


class Student(models.Model):
    gender = models.ForeignKey(Gender, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, blank=True, null=True)
    name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    activ = models.BooleanField(default=False)
    price = models.IntegerField(default=0)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        q = Student.objects.filter(group=self.group)
        if q.count() < self.group.student_count and q.count() != self.group.student_count:
            return super().save(*args, **kwargs)
        else:
            raise SystemError(f"Student qo'shish chegaralangan! maksimum {self.group.student_count}!")


class Registration(models.Model):
    gender = models.ForeignKey(Gender, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    age = models.IntegerField()
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    register = models.BooleanField(default=False)





