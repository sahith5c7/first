from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def Jampandu(request):
    return HttpResponse("<h1><marquee> Hi Jampandu</h1></maequee>")

def Jigelrani(request):
    return HttpResponse(" <h1><marquee>Hello</h1></marquee>")