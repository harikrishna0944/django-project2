from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def first(reqest):
    return HttpResponse("fist view of app2")
def second(reqest):
    return HttpResponse("second view of app2")

