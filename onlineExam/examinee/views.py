from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from examinee import models

def newExaminee(request):
    return render(request,'examinee/newExaminee.html')
    
def examineeRegistration(request):
    e=models.examinee()
    e.name=request.POST['Name']
    e.rollno=request.POST['Rollno']
    e.