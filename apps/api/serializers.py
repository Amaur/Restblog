from rest_framework import serializers
from apps.blog.models import Comment,Post, Tag, Category
from apps.account.models import UserProfile
from django.db.models import Count
from django.contrib.auth.models import User

class CategorySerializer(serializers.ModelSerializer):
    #code
    nbr_post = serializers.SerializerMethodField("NumPost")
    
    def NumPost(self,Category):
        
        return Post.objects.filter(category__title=Category.title).count()
    class Meta:
        model = Category
        fields = ("id","title","description","nbr_post")
        
class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields =('id','slug')

class PostSerializer(serializers.ModelSerializer):
    nbr_comment = serializers.SerializerMethodField("numComment")
    detail = serializers.SerializerMethodField("detailurl")
    def numComment(self, Post):
        return Post.comment_set.all().count()
    def detailurl(self, Post):
        return "http://localhost:8000/api/v1/post/"+Post.slug+"/"#str(Post.id)+"/"
    
    class Meta:
        model = Post
        fields = ('id','author','category','title','intro','slug','detail','created_date','likes','nbr_comment')
        
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id','username','first_name','last_name','email','is_active')
    def create(self, validated_data):
        user = User(
            username=validated_data['username']
        )
        user.set_password(validated_data['password'])
        user.save()
        profile = UserProfile(user=user)
        profile.save()
        return user
        

class ProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = UserProfile
        fields = ('id','image','user')

class PostDetailSerializer(serializers.ModelSerializer):
    nbr_comment = serializers.SerializerMethodField("numComment")
    author = UserSerializer()
    category = CategorySerializer()
    tags = TagSerializer(many=True)
    def numComment(self, Post):
        return Post.comment_set.all().count()
    
    class Meta:
        model = Post
        fields = ('id','author','category','title','intro','text','slug','created_date','created_time','published','updated_date','likes','nbr_comment','tags')

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
    
    


    
    

        
