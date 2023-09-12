from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def first(request):
    return HttpResponse("<h1>Hello world</h1>") 

def second(request):
    return HttpResponse("<input type='text' required ><br><button>submit</button>")

def testview(request):
    name="ajith"
    names=["anu","arun","raju","evani"]
    return render(request,"test.html",{"data":name,"list_name":names})

def log(request):
    return render(request,"login.html")
