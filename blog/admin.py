from django.contrib import admin
from .models import Post, Contact
# Register your models here.


@admin.register(Post)
class PostModelAdmin(admin.ModelAdmin):
    list_display = ['id' ,'title','desc']


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_disply = ['id','full_name','email','comment']