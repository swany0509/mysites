from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.http import HttpResponse

# Create your views here.

def add_two_nums(num1,num2):
    return int(num1)+int(num2)

def add(request):
    return HttpResponse(add_two_nums(request.Get["number1"],request.Get["number2"]))


