from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    category = models.CharField(
        max_length=50,
        verbose_name='Categoria'  
    )
    short_name = models.CharField(
        max_length=50,
        verbose_name='Nombre corto'
    )
    description = models.CharField(
        max_length=200,
        verbose_name='Descripción'
    )

    def __str__(self):
        return self.category

class Professor(User):
    title = models.CharField(
        max_length=50,
        verbose_name='Nombre'
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        verbose_name='Categoria',
        null=True,
        blank=True
    )
    employee_number = models.IntegerField(
        verbose_name='Número de empleado'
    )

    def __str__(self):
        return self.employee_number


class Student(User):
    enrollment = models.CharField(
        max_length=12,
        verbose_name='Matrícula'
    )

    def __str__(self):
        return self.enrollment
