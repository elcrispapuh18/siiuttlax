from django.db import models

# Create your models here.
class Semester(models.Model):
        semester = models.IntegerField(unique=True)  
        semester_name = models.CharField(max_length=50)

        def __str__(self):
            return self.semester_name
class Period(models.Model):
        period = models.CharField(max_length=25)
        year = models.CharField(max_length=4)
        cycle = models.CharField(max_length=11)
        is_active = models.BooleanField(default=True)

        def __str__(self):
            return f"{self.period} {self.year} {self.cycle}"