from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from examiner import models


def examinerLogin(request):
    res=render(request,'examiner/examinerLogin.html')
    return res

def examinerLoginValidate(request):
    userName=request.POST['username']
    passWord=request.POST['password']
    try:
        Examiner=models.examiner.objects.get(username=userName,password=passWord)
        request.session['username']=userName
        res=render(request,'examiner/examinerWelcome.html',{'User':userName})
        return res
    except:
        s="http://localhost:8000/examiner/examiner-login/"
        return HttpResponseRedirect(s)

def decor_login(fun):
    def modified_fun(request):
        if 'username' in request.session.keys():
            return fun(request)
        else:
            return HttpResponseRedirect('http://localhost:8000/examiner/examiner-login/')
    return modified_fun

@decor_login
def examinerQuestionSet(request):
    user=request.session['username']
    res=render(request,'examiner/setquestion.html',{'User':user})
    return res

@decor_login
def examinerQuestionSave(request):
    q=models.questionbank()
    q.qno=request.POST['qn']
    q.que=request.POST['question']
    q.a=request.POST['A']
    q.b=request.POST['B']
    q.c=request.POST['C']
    q.d=request.POST['D']
    q.mark=0
    q.save()
    return HttpResponseRedirect('http://localhost:8000/examiner/question-view/')

@decor_login
def examinerQuestionView(request):
    questions=models.questionbank.objects.all()
    res=render(request,'examiner/questionview.html',{'Questions':questions})
    return res

@decor_login
def examinerQuestionUpdate(request):
    q=models.questionbank.objects.get(qno=request.GET['id'])
    res=render(request,'examiner/questionUpdate.html',{'Que':q})
    return res

@decor_login
def examinerQuestionUpdation(request):
    q=models.questionbank()
    q.qno=request.POST['qno']
    q.que=request.POST['que']
    q.a=request.POST['a']
    q.b=request.POST['b']
    q.c=request.POST['c']
    q.d=request.POST['d']
    q.mark=request.POST['mark']
    q.save()
    return HttpResponseRedirect('http://localhost:8000/examiner/question-view/')

@decor_login
def examinerQuestionDelete(request):
    q=models.questionbank.objects.get(qno=request.GET['id'])
    q.delete()
    return HttpResponseRedirect('http://localhost:8000/examiner/question-view/')

def examinerLogout(request):
    del request.session['username']
    return HttpResponseRedirect('http://localhost:8000/')


