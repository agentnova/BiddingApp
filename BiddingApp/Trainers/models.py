from django.db import models
from Institution.models import SkillModel


# Create your models here.

class SkillFilterModel(models.Model):
    Skill = models.ForeignKey(SkillModel, on_delete=models.CASCADE)

    def __str__(self):
        return self.Skill


class JobApplyModel(models.Model):
    choices = (
        ("applied", "applied"), ("accepted", "accepted"), ("rejected", "rejected")
    )
    title = models.CharField(max_length=100)
    skill = models.CharField(max_length=100)
    user = models.CharField(max_length=120)
    first_name = models.CharField(max_length=120)
    email = models.CharField(max_length=120)
    phone = models.IntegerField()
    address = models.CharField(max_length=120)
    status = models.CharField(max_length=100,choices=choices, default="applied")

    def __str__(self):
        return self.title
