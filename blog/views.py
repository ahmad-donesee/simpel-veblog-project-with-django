from django.shortcuts import render,redirect
from django.urls import reverse,reverse_lazy
from . models import Blog,Comment
from . forms import BlogForm,CommentForm
from django.contrib.auth.models import User
from django.contrib import messages
# Create your views here.

def blog_list(request):
    form=BlogForm()
    list=Blog.objects.all()
    
    if request.method=="POST":
        form=BlogForm(request.POST)
        if form.is_valid():
            form2=form.save(commit=False)
            form2.author = request.user
            form2.save()
            return redirect('blog:blog_list')
    else:
        form=BlogForm()
        return render(request,'blog/blog_home.html',{'blogs':list,"form":form})

def blog_detail(request,id):
    form=CommentForm()
    list=Blog.objects.get(id=id)
    comment=Comment.objects.filter(blog__id=id)
    if request.method=="POST":
        form=CommentForm(request.POST)
        if form.is_valid():
            list=Blog.objects.get(id=id)
            name2=User.objects.get(username=request.user.username)
            # name=form.cleaned_data['name']
            content=form.cleaned_data['content']
            new_comment=Comment(name=name2,content=content,blog=list)
            new_comment.save()
            form=CommentForm()
            # return render(request,'blog/blog_detail.html',{'blogs':list,"comment":comment,"form":form})
            return redirect(reverse("blog:blog_detail",kwargs={"id":id}))
            
    else:
        form=CommentForm()
        return render(request,'blog/blog_detail.html',{'blogs':list,"comment":comment,"form":form})



def delete_blog(request,id):
    blog=Blog.objects.get(id=id)
    user=User.objects.get(username=request.user.username)
    if user==blog.author or request.user.is_superuser :
        blog.delete()
        return redirect('blog:blog_list')
    
    
def update_blog(request,id):
    blog=Blog.objects.get(id=id)
    if request.method=="POST":
        form=BlogForm(request.POST)
        if form.is_valid():
            title=form.cleaned_data["title"]
            content=form.cleaned_data["content"]
            newblog=Blog(content=content,title=title,author=blog.author)
            newblog.save()
            blog.delete()
            # return redirect(reverse("blog:blog_detail",kwargs={'id':newblog.id}))
            return redirect("blog:blog_list")
            
    else:
        form=BlogForm()
        return render(request,"blog/update_blog.html",{"form":form,'blog':blog})
        
# ,spoiler=True