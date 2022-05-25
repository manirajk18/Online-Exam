from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect

def homepage(request):
    res=render(request,"home/home.html")
    return res

