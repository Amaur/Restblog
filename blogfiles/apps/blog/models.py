from django.db import models
from django_markdown.models import MarkdownField
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
import datetime

# Create your models here.
class Tag(models.Model):
    #code
    slug = models.SlugField(max_length=40,unique=True)
    
    def __str__(self):
        return self.slug

class Category(models.Model): 
    title = models.CharField(max_length=200,unique=True) 
    slug = models.SlugField(max_length=40, unique=True) 
    description = models.TextField() 
    class Meta: 
        verbose_name_plural = "Categories"
        
    def __unicode__(self): 
        return self.title
    
    def get_absolute_url(self):
        return "/categories/%s/" % self.slug



class Post(models.Model):
    #code
    title = models.CharField(max_length=200)
    created_date = models.DateField(auto_now_add=True)
    created_time = models.TimeField(auto_now_add=True)
    #updated = models.DateTimeField(auto_now=True)
    updated_date = models.DateField(auto_now=True)
    updated_time = models.TimeField(auto_now=True)
    published = models.BooleanField(default=False)
    slug = models.CharField(max_length=200,unique=True)
    intro    = models.TextField(max_length = 700)
    likes    = models.IntegerField(default=0)
    text = MarkdownField()
    category = models.ForeignKey(Category, blank=True, related_name="posts")
    tags = models.ManyToManyField(Tag)
    author = models.ForeignKey(User)
    
    def save(self):
        date = datetime.datetime.today()
        self.slug = str(self.created_date)+"-"+slugify(self.title)
        super(Post,self).save()
        
    class Meta:
        verbose_name        = "Blog post"
        verbose_name_plural = "Blog posts"
        ordering = ['-created_date']
    

class Comment(models.Model):
    #code
    name = models.CharField(max_length=42)
    email = models.EmailField(max_length=75)
    #website = models.URLField(max_length=200, null=True, blank=True)
    likes    = models.IntegerField(default=0)
    text = models.TextField()
    post = models.ForeignKey(Post,related_name="comments")
    created = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        #code
        ordering = ['created']
    
    

class CategoryToPost(models.Model):
    post = models.ForeignKey(Post)
    category = models.ForeignKey(Category)


