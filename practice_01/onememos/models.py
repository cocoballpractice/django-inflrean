from django.db import models

# Create your models here.
class Memo(models.Model):

    # PK는 따로 작성하지 않아도 된다 (Django에서 PK를 알아서 생성을 해주므로)
    description = models.CharField(max_length=200) # @Column(length = 200) 느낌
    created_at = models.DateTimeField(auto_now_add=True) # @CreatedDate 느낌

    # models.py 작성 후 어드민 사이트에 반영을 위해 admin.py를 열고 추가 작성이 필요

    def __str__(self):
        return self.description