from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField

from management.managers import TeacherManager


class Teacher(AbstractUser):
    username = None
    phone = PhoneNumberField(unique=True)
    class_rel = models.ForeignKey('Class', on_delete=models.CASCADE, null=True, blank=True)
    subject = models.CharField(max_length=30)

    USERNAME_FIELD = 'phone'
    REQUIRED_FIELDS = []

    objects = TeacherManager()

    def __str__(self):
        return self.phone.__str__()


class TeacherProfile(models.Model):
    user = models.OneToOneField(Teacher, on_delete=models.CASCADE)


class Student(models.Model):
    SEX_CHOICES = [
        ('m', 'm'),
        ('f', 'f'),
    ]
    name = models.CharField(max_length=50)
    email = models.EmailField()
    birth_date = models.DateField()
    class_rel = models.ForeignKey('Class', on_delete=models.CASCADE, null=True, blank=True)
    address = models.CharField(max_length=50)
    sex = models.CharField(max_length=1, choices=SEX_CHOICES, default='м')
    image = models.ImageField(upload_to='student_photos/', null=True, blank=True)

    def __str__(self):
        return self.name


class Class(models.Model):
    name = models.CharField(max_length=40)
    teacher_rel = models.ForeignKey('Teacher', on_delete=models.CASCADE, null=True, blank=True)
    students = models.ManyToManyField(Student, blank=True)

    def __str__(self):
        return self.name


class School(models.Model):
    name = models.CharField(max_length=30)
    classes = models.ManyToManyField('Class', blank=True)

    def __str__(self):
        return self.name

