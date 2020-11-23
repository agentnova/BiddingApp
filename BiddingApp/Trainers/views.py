from django.contrib.auth import authenticate, login as djangologin, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from Trainers.forms import *
from Institution.models import *
from Institution.models import SkillModel


# Create your views here.


def trainerRegister(request):
    form = TrainerRegisterForm
    context = {}
    context["form"] = form
    if request.method == "POST":
        form = TrainerRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("tlogin")
        else:
            context["form"] = form
            return render(request, "trainer/register.html", context)
    return render(request, "trainer/register.html", context)


def trainerLogin(request):
    form = TrainerLoginForm
    context = {}
    context["form"] = form
    if request.method == "POST":
        form = TrainerLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(request, username=username, password=password)
            if user:
                djangologin(request, user)
                return redirect("home")
            else:
                context["form"] = form
                return render(request, "trainer/login.html", context)
        else:
            context["form"]=form
    return render(request, "trainer/login.html", context)

@login_required(login_url='tlogin')
def trainerHome(request):
    return render(request, "trainer/trainerhome.html")

@login_required(login_url='tlogin')
def viewalljobs(request):
    jobs = JobModel.objects.all()
    form = SkillFilterForm
    context = {}
    context["jobs"] = jobs
    context["form"] = form
    if request.method == "POST":
        form = SkillFilterForm(request.POST)
        if form.is_valid():
            skill = form.cleaned_data.get("Skill")
            jobs = JobModel.objects.filter(skill=skill)
            context["jobs"] = jobs
            return render(request, "trainer/jobs.html", context)
    return render(request, "trainer/jobs.html", context)

@login_required(login_url='tlogin')
def applyjob(request, pk):
    job = JobModel.objects.get(id=pk)
    form = JobApplyForm(
        initial={"title": job.title, "skill": job.skill, "user": request.user, "first_name": request.user.first_name,
                 "email": request.user.email})
    context = {}
    context["form"] = form
    if request.method == "POST":
        form = JobApplyForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("appliedjobs")
        else:
            context["form"] = form
            return render(request, "trainer/jobapply.html", context)
    return render(request, "trainer/jobapply.html", context)

@login_required(login_url='tlogin')
def appliedjobs(request):
    jobs = JobApplyModel.objects.filter(user=request.user)
    context = {}
    context["jobs"] = jobs
    return render(request, "trainer/appliedjobs.html", context)

@login_required(login_url='tlogin')
def logoutview(request):
    logout(request)
    return redirect("tlogin")


