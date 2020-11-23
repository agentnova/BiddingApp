"""BiddingApp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from Institution.views import *

urlpatterns = [
    path("addskills/", skills, name="skills"),
    path("deleteskill/<int:pk>", deleteskill, name="deleteskill"),
    path("editskill/<int:pk>", editskill, name="editskill"),
    path("jobcreate/", jobCreate, name="jobcreate"),
    path("viewjobs/", viewjobs, name="viewjob"),
    path("deletejob/<int:pk>", deletejob, name="deletejob"),
    path("editjob/<int:pk>", editjob, name="editjob"),
    path("", Institutionhome, name="homepage"),
    path("candidates/", Candidates, name="candidates"),
    path("viewcandidate/<int:pk>", viewcandidate, name="candidateview"),
    path("selected/", selected, name="selected"),
    path("viewselected/<int:pk>",viewSelected,name="viewselected")
]
