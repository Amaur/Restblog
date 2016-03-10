from rest_framework import serializers
from apps.blog.models import Comment,Post, Tag, Category
#from apps.account.models import UserProfile
from django.db.models import Count
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate 

class PostSerializer(serializers.ModelSerializer):
   # nbr_comment = serializers.SerializerMethodField("numComment")
    detail = serializers.SerializerMethodField("detailurl")
    def numComment(self, Post):
        return 1#Post.comment_set.all().count()
    def detailurl(self, Post):
        return "http://localhost:8000/api/post/"+Post.slug+"/"#str(Post.id)+"/"
    
    class Meta:
        model = Post
        fields = ('id','author','category','title','intro','slug','detail','created_date','likes')#,'nbr_comment')
        

class CategorySerializer(serializers.ModelSerializer):
    #code
    nbr_post = serializers.SerializerMethodField("NumPost")
    
    def NumPost(self,Category):
        
        return Post.objects.filter(category__title=Category.title).count()
    class Meta:
        model = Category
        fields = ("id","title","description","nbr_post")

class CategoryDetailSerializer(serializers.ModelSerializer):
   
    posts = PostSerializer(many=True)
    nbr_post = serializers.SerializerMethodField("NumPost")
    
    def NumPost(self,Category):
        return Post.objects.filter(category__title=Category.title).count()
    
    class Meta:
        model = Category
        fields = ("id","title","description","nbr_post","posts")
    

    
class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields =('id','slug')


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username','first_name','last_name','email')

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ("name","email","likes","text","created","post")
    def create(validated_data):
        comment = Comment(
            name = validated_data['name'],
            email = validated_data['email'],
            likes =0,
            text = validated_data['text'],
            post = validated_data['post']
        )
        comment.save()
        return comment   



class PostDetailSerializer(serializers.ModelSerializer):
    
    author = UserSerializer()
    category = CategorySerializer()
    tags = TagSerializer(many=True)
    comments = CommentSerializer(many=True)
    class Meta:
        model = Post
        fields = ('id','author','category','title','intro','text','slug','created_date','created_time','published','updated_date','likes','tags','comments')
    

    
    


    
    

        
