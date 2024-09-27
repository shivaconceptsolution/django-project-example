from django.shortcuts import render
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