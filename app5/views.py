from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def macha(request):
    return render(request,'macha.html')