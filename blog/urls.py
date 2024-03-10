from django.urls import path
from . views import blog_list,blog_detail,delete_blog,update_blog

app_name="blog"

urlpatterns = [
    path("",blog_list, name="blog_list"),
    path("<int:id>/",blog_detail, name="blog_detail"),
    path("delete/<int:id>/",delete_blog,name="delete_blog"),
    path("update/<int:id>/",update_blog,name="update_blog"),
    
]
