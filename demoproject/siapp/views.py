from django.shortcuts import render,redirect
from django.http import HttpResponse
def index(request):
    if request.method=="POST":
        print("hello")
        p=request.POST["p"]
        r=request.POST["r"]
        t=request.POST["t"]
        si = (float(p)*float(r)*float(t))/100
        return HttpResponse("result is "+str(si))
    return render(request,"siapp/index.html")
def welcome(request):
    return redirect("index")

def radioexample(request):
    if request.method=="POST":
        coursename=request.POST.get("course")
        return render(request,"siapp/course.html",{"key":coursename})
    return render(request,"siapp/course.html")
def checkboxexample(request):
    if request.method=="POST":
        courselist = request.POST.getlist("course")
        data=''
        for c in courselist:
            data+=c+' '
        return render(request,"siapp/checkboxexample.html",{"key":data})
    return render(request,"siapp/checkboxexample.html")