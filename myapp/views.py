from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def hello(request):
    return HttpResponse("<h2>Hello Moondo</h2>")

def about(request):
    return HttpResponse("<h2>Ab0ut</h2>")