from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=200,default='title')
    author = models.CharField(max_length=100,default='author')
    description = models.CharField(max_length=2000,default='description')




class ContactModel(models.Model):
    name = models.CharField(max_length=100,default='name')
    email= models.CharField(max_length=100,default='email')
    your_message = models.CharField(max_length=2000,default='your_message')




