from django.db import models
class students(models.Model):
        name1=models.CharField(max_length=50)
        college1=models.CharField(max_length=100)
        course1=models.CharField(max_length=30)
# Create your models here.
def __str__(self):
        return self.name1