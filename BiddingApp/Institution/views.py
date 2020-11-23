from django.shortcuts import render, redirect
from Institution.models import SkillModel, JobModel
from Institution.forms import SkillForm, Jobform,AppliedJobform
from Trainers.models import JobApplyModel


# Create your views here.

def skills(request):
    obj = SkillModel.objects.all()
    form = SkillForm()
    context = {}
    context["skills"] = obj
    context["form"] = form
    if request.method == "POST":
        form = SkillForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, "institution/skills.html", context)
    return render(request, "institution/skills.html", context)


def deleteskill(request, pk):
    obj = SkillModel.objects.get(id=pk).delete()
    return redirect("skills")


def editskill(request, pk):
    obj = SkillModel.objects.get(id=pk)
    obj2 = SkillModel.objects.all()
    form = SkillForm(instance=obj)
    context = {}
    context["form"] = form
    context["skills"] = obj2
    if request.method == "POST":
        form = SkillForm(instance=obj, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect("skills")
    return render(request, "institution/skills.html", context)


def jobCreate(request):
    form = Jobform
    context = {}
    context["form"] = form
    if request.method == "POST":
        form = Jobform(request.POST)
        if form.is_valid():
            form.save()
            return redirect("viewjob")
    return render(request, "institution/job.html", context)


def viewjobs(request):
    obj = JobModel.objects.all()
    context = {}
    context["jobs"] = obj
    return render(request, "institution/viewjob.html", context)


def deletejob(request, pk):
    obj = JobModel.objects.get(id=pk).delete()
    return redirect("viewjob")


def editjob(request, pk):
    obj = JobModel.objects.get(id=pk)
    form = Jobform(instance=obj)
    context = {}
    context["form"] = form
    if request.method == "POST":
        form = Jobform(instance=obj, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect("viewjob")
    return render(request, "institution/editjob.html", context)

def Institutionhome(request):
    return render(request,"institution/home.html")

def Candidates(request):
    candidates=JobApplyModel.objects.filter(status="applied")
    context={}
    context["candidates"]=candidates
    return render(request,"institution/candidates.html",context)

def selected(request):
    candidates=JobApplyModel.objects.filter(status="accepted")
    context = {}
    context["candidates"] = candidates
    return render(request, "institution/selected.html", context)

def viewcandidate(request,pk):
    candidates=JobApplyModel.objects.get(id=pk)
    form=AppliedJobform(instance=candidates)
    context={}
    context["form"]=form
    if request.method=="POST":
        form=AppliedJobform(instance=candidates,data=request.POST)
        if form.is_valid():
            form.save()
            return redirect("candidates")
        else:
            context["form"]=form
            return render(request,"institution/viewcandidate.html",context)
    return render(request,"institution/viewcandidate.html",context)

def viewSelected(request,pk):
    candidate=JobApplyModel.objects.get(id=pk)
    context={}
    context["candidate"]=candidate
    return render(request,"institution/viewselectedcandidate.html",context)



