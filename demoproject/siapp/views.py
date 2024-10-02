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
        return render(request,"siapp/checkboxexample.html",{"key":data,"key1":courselist})
    return render(request,"siapp/checkboxexample.html")
def colorexample(request):
    if request.method=="POST":
        color = request.POST.get("color")
        return render(request,"siapp/colorexample.html",{"key":color})
    return render(request,"siapp/colorexample.html")
def feesexample(request):
    if request.method=="POST":
        bfee = request.POST.get("bfee")
        afee = request.POST.getlist("afee")
        coursename=''
        fee=0
        bcourse=bfee.split(':') #["c","2000"]
        coursename+=bcourse[0] + " "
        fee+=int(bcourse[1])
        for data in afee:
            acourse=data.split(':')
            coursename+=acourse[0] + " "
            fee+=int(acourse[1])
        return render(request,"siapp/feesexample.html",{"key1":coursename,"key2":fee})
    return render(request,"siapp/feesexample.html")
def listexample(request):
    if request.method=="POST":
         data = request.POST.getlist("lst")
         s=''
         for item in data:
            s=s+item+" "
         return render(request,"siapp/listexample.html",{"key":s,"key1":data})
    return render(request,"siapp/listexample.html")
def ddlexample(request):
    data = request.POST.get("ddl")
    return render(request,"siapp/ddlexample.html",{"key":data})