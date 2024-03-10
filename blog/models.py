from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Blog(models.Model):
    title = models.CharField(max_length=20)
    author=models.ForeignKey(User, on_delete=models.CASCADE,null=True,blank=True)
    # name=models.CharField(max_length=20)
    content=models.TextField()

    created_at=models.DateTimeField(auto_now_add=True)
    update=models.DateTimeField(auto_now=True)
    slug=models.SlugField()
    
    class Meta:
        verbose_name_plural="وبلاگ ها"
    
    def __str__(self):
        return self.title
    
class Comment(models.Model):
    blog = models.ForeignKey(Blog,on_delete=models.CASCADE,related_name='comments')
    user  = models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    name = models.CharField(max_length=80, null=True, blank=True)
    content=models.TextField( null=True, blank=True)
    
    class Meta:
        verbose_name_plural="نظرات"
    
    def __str__(self):
        return f"{self.name} - {self.user}"
    

    
    