from django.db import models

class Teacher(models.Model):
    name = models.CharField(max_length=20)
    class_name = models.CharField(max_length=20, choices=(
        ('A_class', 'a_class'),
        ('B_class', 'b_class'),
        ('C_class', 'c_class')
    ))

    def __str__(self):
        return self.name

class Pupil(models.Model):
    name = models.CharField(max_length=20)
    birth_date = models.DateField(null=True, blank=True)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)

    def __str__(self):
        return self.name