from django.contrib import admin
from apps.blog import models
from apps.account.models import UserProfile
# Register your models here.

class BlogAdmin(admin.ModelAdmin):
    exclude = ['created_date']
    prepopulated_fields = {'slug': ('title',)}
    #fields = ('title','created_date','intro')

admin.site.register(models.Post,BlogAdmin)
admin.site.register(models.Category)
admin.site.register(models.Tag)
admin.site.register(models.Comment)
admin.site.register(UserProfile)

