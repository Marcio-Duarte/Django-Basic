from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def getTitle(request):
    pageTitle = {'title':"Home"}
    return render(request,'home/index.html',context=pageTitle)