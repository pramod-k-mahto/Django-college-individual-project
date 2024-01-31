from django.contrib import admin
from .models import Blog,ContactModel
@admin.register(Blog)
class BlogModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description','author')
 
 
@admin.register(ContactModel)
class BlogModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email','your_message')
 
 
 