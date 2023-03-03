from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('onememos/', include('onememos.urls')), # 하위 앱에서 처리할 url path 추가
    path('admin/', admin.site.urls),
]
