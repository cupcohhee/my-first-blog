from http.client import HTTPResponse
from re import X
from django.shortcuts import render
from django.http import HttpResponse

# request -> response
# request handler
# action 
def calculate():
    x = 1
    y = 2
    return x
def say_hello(request):
    
    x = calculate()
    return render(request,'hello.html' , {'name': 'Lyon'})




# Create your views here.
