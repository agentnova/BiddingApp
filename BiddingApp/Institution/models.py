from django.db import models


# Create your models here.

class SkillModel(models.Model):
    skill = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.skill


class JobModel(models.Model):
    skill = models.ForeignKey(SkillModel, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    experience = models.CharField(max_length=100, default="1 year")
    salary = models.IntegerField()

    def __str__(self):
        return self.title
