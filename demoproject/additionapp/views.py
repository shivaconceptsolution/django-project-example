from django.shortcuts import render
from django.http import HttpResponse

def addition(request):
    if request.method=="POST":
        a = request.POST["txtnum1"]
        b = request.POST["txtnum2"]
        c = int(a)+int(b)
        return HttpResponse("Result is "+str(c))
    else:
      return render(request,"additionapp/add.html")
