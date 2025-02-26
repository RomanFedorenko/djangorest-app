from django.db import models

# Create your models here.
class Student(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    score = models.IntegerField()

    def __str__(self):
        return self.name+":"+str(self.score)