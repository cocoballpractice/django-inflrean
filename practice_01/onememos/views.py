from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def main(request): # 기본적인 요청 흐름 url 요청 -> urls.py -> main()
    #return HttpResponse("안녕 my 월드야")
    return render(request, 'main.html') # 템플릿 파일명 (앱 폴더 하위 templates에 있다면 경로 지정 하지 않아도 됨)

def detail(request):
    return HttpResponse("안녕 my detail 월드야")

def createMemo(request):
    # request 객체는 사용자가 폼 페이지를 통해서 입력한 폼 데이터 값들을 받는다
    # request.GET, request.POST, request.COOKIE -> 딕셔너리형 데이터 GET, POST, COOKIE 정보들을 받음

    memoContent = request.POST['memoContent']

    return HttpResponse("create memo = " + memoContent)