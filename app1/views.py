from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def hari(request):
    return HttpResponse("<h1><marquee>hari</marquee></h1> ")
def krishna(request):
    return HttpResponse("<i><button> krishna</button></i>")
