from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def getTitle(request):
    pageTitle = {'title':"Users"}
    return render(request,'user/index.html',context=pageTitle)
