from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return render(request,"home/index.html")

def about(request):
    return HttpResponse("<h1> about us page  </h1>")

def contact(request):
    return HttpResponse("<h1> contact page </h1>")


def service(request):
    return HttpResponse("<h1> Service page </h1>")
# Create your views here.