from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField()

    create_at = models.DateTimeField(auto_now_add=True) 
    # auto_now_add = 시간 자동 생성
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'[글 번호: {self.pk}] 제목: {self.title}'
    
    def get_absolute_url(self):
        return f'/blog/{self.pk}/'