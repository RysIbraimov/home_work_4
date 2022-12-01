from django.db import models

# Create your models here.
class Course(models.Model):
    name = models.CharField(max_length=30, verbose_name='название курса')
    mentor = models.CharField(max_length=20, verbose_name='Имя ментора')
    month = models.IntegerField(default=6, verbose_name='Длительность курсов')

    def __str__(self):
        return self.name

class Student(models.Model):
    name = models.CharField(max_length=20, verbose_name='ФИО студента')
    laptop = models.CharField(max_length=20, choices=(
        ('mac', 'Macbook'),
        ('linux', 'linux'),
        ('windows', 'windows')
    ), verbose_name='операйионная система')
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
