from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.urls import reverse

from onememos.models import Memo

# Create your views here.

def main(request): # 기본적인 요청 흐름 url 요청 -> urls.py -> main()

    lists = Memo.objects.all() # Memo 객체 전부 조회
    data = {'lists' : lists} # 반드시 딕셔너리 형태로 저장하여 템플릿 파일로 전달해야 함 (map.addAttribute() 느낌)

    return render(request, 'main.html', data) # 템플릿 파일명 (앱 폴더 하위 templates에 있다면 경로 지정 하지 않아도 됨)

def detail(request):
    return HttpResponse("안녕 my detail 월드야")

def createMemo(request):
    # request 객체는 사용자가 폼 페이지를 통해서 입력한 폼 데이터 값들을 받는다
    # request.GET, request.POST, request.COOKIE -> 딕셔너리형 데이터 GET, POST, COOKIE 정보들을 받음

    memoContent = request.POST['memoContent']

    # DB 입력
    article = Memo(description = memoContent)
    article.save() # 별도의 DAO 없이 바로 가능하구나....

    # 리다이렉트를 위한 HttpResponseRedirect, reverse
    # redirect() - 특정 url로 리다이렉션
    # reverse() - URL을 역으로 계산하여 path가 변경되어도 url을 외울 필요가 없음, urls.py에서 만든 URL Patterns의 name을 이용, name을 통해 해당 name의 url을 반환
    # name 정보 틀릴 경우 페이지 에러 발생

    return HttpResponseRedirect(reverse('main'))

