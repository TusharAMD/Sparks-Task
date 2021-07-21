from django.shortcuts import render

def index(request):
    return render(request,"payment/index.html",{})
    
def about(request):
    return render(request,"payment/about.html",{})

def donate(request):
    return render(request,"payment/donate.html",{})
    
def contact(request):
    return render(request,"payment/contact.html",{})
# Create your views here.
