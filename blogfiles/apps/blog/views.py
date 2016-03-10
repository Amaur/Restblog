from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from apps.api.v1.serializers import PostSerializer
from rest_framework.response import Response
from .models import Post

# Create your views here.
def Index(request):
    return render(request,"blog/index.html")

def Blog(request):
    return render(request, "blog/blog.html")

def Recent(request,format=None):
    posts = Post.objects.all()[:5]
    serializer = PostSerializer(posts, many=True)
    print(serializer.data)
    return HttpResponse(serializer.data)

def About(request):
    return render(request, "blog/about.html")

def Contact(request):
    return render(request, "blog/contact.html")

def Projet(request):
    return render(request, "blog/projets.html")

def Read(request,slug):
    slug = slug
    return render(request, "blog/read.html",{"slug":slug})

@login_required
def AddComment(request,pk):
    pass
@login_required
def Post_likes(request,pk):
    pass

@login_required
def Comment_likes(request, pk):
    pass







