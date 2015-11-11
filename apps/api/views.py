from django.shortcuts import render
from django.http import Http404
from django.http import HttpResponse
from apps.blog.models import *
from .serializers import CategorySerializer, UserSerializer, PostSerializer,ProfileSerializer,PostDetailSerializer, CommentSerializer
from django.contrib.auth.models import User
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from apps.account.models import UserProfile
from django.contrib.auth.models import User

# Create your views here.
def Index(request):
    return HttpResponse("Hello world, bravo!")


class UserList(APIView):
    """ list of all users """
    def get(self, request,format=None):
        users = User.objects.all()
        serializer = UserSerializer(users,many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = UserSerializer(request.data)
        if(serializer.is_valid()):
            serializer.create(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, ):
        pass
    
    

class UserProfil(APIView):
    """ detail of some ramdom user """
    def get_object(self, pk):
        try:
            return User.objects.get(id=int(pk))
        except User.DoesNotExist:
            raise Http404
    
    def get(self, request, pk, format=None ):
        user = self.get_object(pk)
        profile = UserProfile.objects.get(user=user)
        serializer = ProfileSerializer(profile)
        return Response(serializer.data)
    def post(self, request, pk, format=None):
        user = self.get_object(pk)
        profile = UserProfile.objects.get(user=user)
        #data = {'image':request.data['file']}
        profile.image= request.data['file']
        profile.save()
        
        

class CategoryList(APIView):
    """ List of all categories """
    def get_object(self):
        try:
            return Category.objects.all()
        except Category.DoesNotExist:
            raise Http404
    def get(self, request,format=None):
        categories = self.get_object()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)

class CommentList(APIView):
    """ get comment for some user """
    def get_object(self, pk):
        try:
            return Post.objects.get(id=int(pk))
        except Post.DoesNotExist:
            raise Http404
        
    def get(self, request, pk, format=None):
        post = self.get_object(pk=int(pk))
        comments = post.comment_set.all()
        serializer = CommentSerializer(comments,many=True)
        return Response(serializer.data)
    
    def post(self, request, pk, format=None):
        serializer = CommentSerializer(data=request.data)
        if(serializer.is_valid()):
            serializer.create(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




class PostList(APIView):
    """ class for display all posts and create new one """
    def get(self, request, format=None ):
        posts = Post.objects.all()
        serializer = PostSerializer(posts,many=True)
        return Response(serializer.data)
    
class PostDetail(APIView):
    """ Detail of a post """
    def get_object(self, slug):
        try:
            return Post.objects.get(slug=slug)
        except Post.DoesNotExist:
            raise Http404
    
    def get(self, request, slug, format=None ):
        post = Post.objects.get(slug=slug)
        serializer = PostDetailSerializer(post)
        return Response(serializer.data)

class RecentPost(APIView):
    """ show last 10  posts """
    def get(self, request, format=None):
        posts = Post.objects.all()[:10]
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)
    
class PostLikes(APIView):
    """ Detail of a post """
    
    def get_object(self, pk):
        try:
            return Post.objects.get(id=int(pk))
        except Post.DoesNotExist:
            raise Http404
    
    def get(self, request, pk, format=None ):
        post = self.get_object(pk)
        likes = post.likes + 1
        post.likes = likes
        post.save()
        return HttpResponse(likes)
    
    def delete(self, request, pk, format=None):
        post = self.get_object(pk)
        likes = post.likes - 1
        post.likes = likes
        post.save()
        return HttpResponse(likes)
    
