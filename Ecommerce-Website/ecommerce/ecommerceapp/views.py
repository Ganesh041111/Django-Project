from django.shortcuts import render
from ecommerceapp.models import Contact
from django.contrib import messages
# Create your views here.
def index(request):
    return render(request, "index.html")

def contactus(request):
    if request.method=="POST":
        name=request.POST.get("name")
        email=request.POST.get("email")
        desc=request.POST.get("desc")
        pnumber=request.POST.get("pnumber")
        myquery=Contact(name=name,email=email,desc=desc,phonenumber=pnumber)
        myquery.save()
        messages.info(request, "We will get back to you soon..")
        return render(request, "contactus.html")
    return render(request, "contactus.html")

def aboutus(request):
    return render(request, "aboutus.html")
