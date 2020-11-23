from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm
from django import forms
from Trainers.models import *


class TrainerRegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["first_name", "last_name", "email", "username", "password1", "password2"]
        widgets = {
            "first_name": forms.TextInput(attrs={"class": "form-control"}),
            "last_name": forms.TextInput(attrs={"class": "form-control"}),
            "email": forms.TextInput(attrs={"class": "form-control"}),
            "username": forms.TextInput(attrs={"class": "form-control"}),
            "password1": forms.TextInput(attrs={"class": "form-control"}),
            "password2": forms.TextInput(attrs={"class": "form-control"})
        }

    def clean(self):
        cleaned_data = super().clean()
        uname = cleaned_data.get("username")
        email = cleaned_data.get("email")
        username = User.objects.filter(username=uname)
        mail = User.objects.filter(email=email)
        if username:
            msg = "Username already exist"
            self.add_error("username", msg)
        if mail:
            msg = "Email already registered"
            self.add_error("email", msg)


class TrainerLoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control"}), max_length=100)
    password = forms.CharField(widget=forms.PasswordInput(attrs={"class": "form-control"}), max_length=100)

    def clean(self):
        cleaned_data = super().clean()
        uname = cleaned_data.get("username")
        pwd = cleaned_data.get("password")
        username = User.objects.filter(username=uname)
        if username:
            user = authenticate(username=uname, password=pwd)
            if user is None:
                msg = "Invalid password"
                self.add_error("password", msg)
        else:
            msg = "Invalid username"
            self.add_error("username", msg)


class SkillFilterForm(ModelForm):
    class Meta:
        model = SkillFilterModel
        fields = "__all__"
        widgets = {
            "Skill": forms.Select(attrs={"class": "form-control"})
        }

    def clean(self):
        print("cleaned")


class JobApplyForm(ModelForm):
    class Meta:
        model = JobApplyModel
        fields = "__all__"
        widgets = {
            "title": forms.TextInput(attrs={"class": "form-control", "readonly": "readonly"}),
            "skill": forms.TextInput(attrs={"class": "form-control", "readonly": "readonly"}),
            "user": forms.TextInput(attrs={"class": "form-control", "readonly": "readonly"}),
            "first_name": forms.TextInput(attrs={"class": "form-control", "readonly": "readonly"}),
            "email": forms.TextInput(attrs={"class": "form-control", "readonly": "readonly"}),
            "phone": forms.NumberInput(attrs={"class": "form-control"}),
            "address": forms.Textarea(attrs={"class": "form-control", "rows": 2}),
            "status": forms.HiddenInput()
        }

    def clean(self):
        cleaned_data = super().clean()
        phone = cleaned_data.get("phone")
        if len(str(phone)) < 10:
            msg = "Not a valid number"
            self.add_error("phone", msg)
