from django.urls import path

from . import views

# 사용자 요청 url 패턴 및 응답 정의
# path(요청 url, 처리 함수)
# controller의 RequestMapping 느낌인듯
# request url이 최상위 urls.py -> app별 urls.py 로 mapping 되는 것 같음
# 사용자가 localhost:8080/onememos로 들어올 경우를 가정하면
# 해당 urls.py가 onememos 내부에 있으므로 추가 path를 적을 필요는 없음

urlpatterns = [
    #path('', views.index, name='index'), #views.py의 함수 매핑. DispatcherServlet -> Controller 확인 및 해당 컨트롤러의 핸들러 메서드로 매핑해주는 느낌
    path('', views.main),
    path('createMemo/', views.createMemo),
    path('detail', views.detail, name='detail') # 앞에 /를 안 붙여도 됨 (자동으로 붙음)
]