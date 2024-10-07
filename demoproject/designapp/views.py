from django.shortcuts import render
def home(request):
    return render(request,"designapp/home.html")
def about(request):
    return render(request,"designapp/about.html")
def services(request):
    return render(request,"designapp/services.html")
def contact(request):
    return render(request,"designapp/contact.html")
def gallery(request):
    return render(request,"designapp/gallery.html")