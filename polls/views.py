from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def index(request):
    return render(request,"polls/index.html") #將index.html頁面拋給使用者
