from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request): # 기본적인 요청 흐름 url 요청 -> urls.py -> index()
    return HttpResponse("안녕 my 월드야")

def detail(request):
    return HttpResponse("안녕 my detail 월드야")