
from django.urls import path
from . import views 

urlpatterns = [
    path('about/',views.about,name='about'),
    path('contact/',views.contact,name='contact'),
    path('createblog/',views.createblog,name='createblog'),
    path('blog/',views.blog,name='blog'),
    path('description/<id>',views.description,name='description'),
    path('delete/<id>',views.delete,name='delete'),
    path('editblog/<id>',views.editblog,name='editblog'),
    path('login/', views.user_login, name='login'),
    path('singup/', views.user_signup, name='singup'),
    path('logout/', views.user_logout, name='logout') 
]
