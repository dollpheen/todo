from django.http import HttpResponse
from random import shuffle
from django.shortcuts import render
from django import forms
    
def index(request):
    return HttpResponse("<h2>Welcome to TODO!</h2><a href='/create'>create user</a><a href = '/login' ><p>login</p></a>")
