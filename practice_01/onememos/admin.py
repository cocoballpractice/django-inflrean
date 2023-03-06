from django.contrib import admin
from onememos.models import Memo # models.py의 Memo class import

# Register your models here.
admin.site.register(Memo) # admin.site에 등록