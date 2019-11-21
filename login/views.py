from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def getTitle(request):
    pageTitle = {'title':"Login"}
    return render(request,'login/index.html',context=pageTitle)
