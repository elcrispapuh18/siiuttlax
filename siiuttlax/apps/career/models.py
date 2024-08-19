from django.db import models

# Create your models here.

class Level(models.Model):
    level = models.CharField(max_length=100)
    short_name = models.CharField(max_length=10)

    def __str__(self):
        return self.short_name
    
class Career(models.Model):
    name = models.CharField(max_length=50)
    level =  models.ForeignKey(Level, on_delete=models.CASCADE)
    shortname = models.CharField(max_length=10)
    director = models.CharField(max_length=100)
    plan = models.CharField(max_length=4)
    status = models.BooleanField()

class Subject(models.Model):
    name = models.CharField(max_length=50)
    career = models.ForeignKey(Career, on_delete=models.CASCADE)
    semester = models.IntegerField()
    total_hours = models.IntegerField()
    hours_semesters = models.IntegerField()
    file = models.CharField(max_length=50)





