from django.shortcuts import render
from django.http import HttpResponse #importing Response
# Create your views here.

def learn_django(request): #request
    return HttpResponse("<h1> Hello Django </h1>")

def learn_python(request):
    return HttpResponse("<h3> Hello Python </h3>")

def learn_math(request):
    b = 4 * 5
    return HttpResponse(f"<h1> Value: {b} <h1>")

def learn_string(request):
    mystr = "Pooja Kulkarni"
    return HttpResponse(f"<h1> Hello: {mystr} <h1>")