from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Привет, Python315!") # вернет страничку с надписью "Привет, мир!" на русском языке.
