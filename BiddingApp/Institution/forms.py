from django.forms import ModelForm
from django import forms
from Institution.models import SkillModel, JobModel
from Trainers.models import JobApplyModel


class SkillForm(ModelForm):
    class Meta:
        model = SkillModel
        fields = "__all__"
        widgets = {
            "skill": forms.TextInput(attrs={"class": "form-control"})
        }

    def clean(self):
        print("cleaned")


class Jobform(ModelForm):
    class Meta:
        model = JobModel
        fields = "__all__"
        widgets = {
            "title": forms.TextInput(attrs={"class": "form-control"}),
            "skill": forms.Select(attrs={"class": "form-control"}),
            "experience": forms.TextInput(attrs={"class": "form-control"}),
            "salary": forms.NumberInput(attrs={"class": "form-control"})
        }
    def clean(self):
        print("cleaned")

class AppliedJobform(ModelForm):
    class Meta:
        model=JobApplyModel
        fields="__all__"
        widgets = {
            "title": forms.TextInput(attrs={"class": "form-control", "readonly": "readonly"}),
            "skill": forms.TextInput(attrs={"class": "form-control", "readonly": "readonly"}),
            "user": forms.TextInput(attrs={"class": "form-control", "readonly": "readonly"}),
            "first_name": forms.TextInput(attrs={"class": "form-control", "readonly": "readonly"}),
            "email": forms.TextInput(attrs={"class": "form-control", "readonly": "readonly"}),
            "phone": forms.NumberInput(attrs={"class": "form-control", "readonly": "readonly"}),
            "address": forms.Textarea(attrs={"class": "form-control", "rows": 2, "readonly": "readonly"}),
            "status": forms.Select(attrs={"class": "form-control"})
        }
