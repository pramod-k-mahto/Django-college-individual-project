from django.shortcuts import render, redirect, get_object_or_404
from .forms import BlogForm,ContactForm, User_Login_Form
from .models import Blog
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.models import User
from django.shortcuts import HttpResponseRedirect
from django.contrib import messages

def home(request):
    return render(request, 'home/home.html')
def about(request):
    return render(request, 'about/about.html')        

def contact(request):
    if request.user.is_authenticated:      
            if request.method == "POST":
                fm = ContactForm(request.POST)
                if fm.is_valid():
                    n = fm.cleaned_data["name"]
                    e = fm.cleaned_data["email"]
                    message=fm.cleaned_data["your_message"]
                    ContactFormData = ContactForm(name=n, email=e,your_message=message)
                    try:
                        ContactFormData.save()
                        print("Data saved successfully")
                        return render(request, 'contact/contact.html',{"form":fm})

                    except Exception as e:
                        print(f"Error saving to the database: {e}")
            else:
                fm = ContactForm()
                return render(request, 'contact/contact.html',{"form":fm})
    else:
        return HttpResponseRedirect('/myblog/login')
      
      
        
def createblog(request):
    if request.user.is_authenticated:
            if request.method == "POST":
                fm = BlogForm(request.POST)
                if fm.is_valid():
                    ti = fm.cleaned_data["title"]
                    des = fm.cleaned_data["description"]
                    author=fm.cleaned_data["author"]
                    print(f"Form data: Title - {ti}, Description - {des}")
                    blogData = Blog(title=ti, description=des,author=author)
                    try:
                        blogData.save()
                        print("Data saved successfully")
                    except Exception as e:
                        print(f"Error saving to the database: {e}")
                    fm = BlogForm()
            else:
                fm = BlogForm()
            data = Blog.objects.all()
            print('hi data got from data base', data)
            return render(request, 'createblog/createblog.html', {'form': fm, 'data': data})
    else:
        return HttpResponseRedirect('/myblog/login')
        
    
    
def blog(request):
    data = Blog.objects.all()
    return render(request, 'blog/blog.html', {'data': data})

def description(request, id):
    
    if request.user.is_authenticated:
            data = get_object_or_404(Blog, pk=id)
            return render(request, 'description/description.html', {'data': data})

    else:
            return HttpResponseRedirect('/myblog/login')
        

def delete(request, id): 
    print("Delete id ", id)
    # Get the Blog object or return a 404 response if not found
    blog_instance = get_object_or_404(Blog, pk=id)

    # Delete the object
    blog_instance.delete()
    # Redirect to the blog list page
    return redirect('createblog')  

def editblog(request,id):
    data = Blog.objects.get(pk=id)
    print(data)
        
    if request.method == "POST":
        fm = BlogForm(request.POST, instance=data)
        if fm.is_valid():
            fm.save()
            return redirect('createblog')
    else:
        fm = BlogForm(instance=data)
    return render(request, 'editblog/editblog.html', {'form': fm, 'data': data})



def user_signup(request):
    if request.method == "POST":
        fm = User_Login_Form(request.POST)
        if fm.is_valid():
            fm.save()
            return HttpResponseRedirect('/myblog/login/')
    else:
        fm = User_Login_Form()
        return render(request, 'singup/singup.html', {'form': fm})

    # Add a default return statement, for example, redirecting to some other URL
    return HttpResponseRedirect('/myblog/login/')


def user_login(request):
    if request.method == 'POST':
        fm = AuthenticationForm(request=request, data=request.POST)
        if fm.is_valid():
            uname = fm.cleaned_data['username']
            upass = fm.cleaned_data['password']
            user = authenticate(username=uname, password=upass)

            if user is not None:
                login(request, user)
                return HttpResponseRedirect('/')
            else:
                messages.error(request, "Invalid username or password.")
    else:
        fm = AuthenticationForm()

    return render(request, 'login/login.html', {'fm': fm})


def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/myblog/login')