from django.shortcuts import render
from .models import post

# Create your views here.
def post_list(request):
    return render(request,'hello.html')
