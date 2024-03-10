from django.contrib import admin
from  .models import Blog,Comment
# Register your models here.

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title','author')
    search_fields = ['title']
    
    class Meta:
        verbose_name_plural="ادمین"
    
    
@admin.register(Comment)
class Comment(admin.ModelAdmin):
    list_display=['name']
    
     