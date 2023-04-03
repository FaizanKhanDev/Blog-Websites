from django.shortcuts import render, HttpResponseRedirect
from .forms import SignForm,LoginForm, Postform
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .models import Post, Contact
from django.contrib.auth.models import Group
from .forms import Contact_Form, EditAdminProfile
# Create your views here.


def home(request):
    posts = Post.objects.all()
    return render(request,'blog/home.html',{'posts':posts})


def about(request):
    return render(request,'blog/about.html')


def contact(request):
    if request.method == 'POST':
        form = Contact_Form (request.POST)
        if form.is_valid():
            uname = form.cleaned_data['full_name']
            em = form.cleaned_data['email']
            com = form.cleaned_data['comment']
            form = Contact(full_name=uname,email=em,comment=com)
            messages.success(request,'Your message has beem Send!! We Will Response Soon please be Patience')
            form.save()
            form = Contact_Form() 
            return HttpResponseRedirect('/contact/')
           

    else:
        form = Contact_Form()
    return render(request,'blog/contact.html',{'form':form})



def dashboard(request):
    if request.user.is_authenticated:
        posts = Post.objects.all()
        user = request.user
        full_name = user.get_full_name()
        gps = user.groups.all()
        return render(request,'blog/dashboard.html',{'posts':posts,'groups':gps,'fullname':full_name})
    else:
        return HttpResponseRedirect('/login/')



def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/')




def user_signup(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = SignForm(request.POST)
            if form.is_valid():
                messages.success(request,'Congratulation! Your Account Has Been Created Successfully')
                user = form.save()
                group = Group.objects.get(name='Author')
                user.groups.add(group) 
        else:
            form = SignForm()
        return render(request,'blog/signup.html',{'form':form})
    else:
        return HttpResponseRedirect('/dashboard/')
   



def user_login(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = LoginForm(request=request,data=request.POST)
            if form.is_valid():
                uname = form.cleaned_data['username']
                upass = form.cleaned_data['password']
                user =  authenticate(username=uname,password=upass)
                if user is not None:
                    login(request,user)
                    messages.success(request,'Logged in Successfully')
                    return HttpResponseRedirect ('/dashboard/')
        else:
            form = LoginForm()
        return render(request,'blog/login.html',{'form':form})

    else:
        return  HttpResponseRedirect('/dashboard/')




# Add Post
def add_post(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = Postform(request.POST)
            if form.is_valid():
                title = form.cleaned_data['title']
                desc = form.cleaned_data['desc']
                pst = Post(title=title,desc=desc)
                pst.save()
                messages.success(request,'Your Post has Been Uploaded')
                form = Postform()
        else:
            form = Postform()
        return render(request,'blog/addpost.html',{'form':form})
    else:
        return HttpResponseRedirect('/login/')

# update Post
def update_post(request, id):
    if request.user.is_authenticated:
        if request.method == 'POST':
            pi = Post.objects.get(pk=id)
            form =  Postform(request.POST, instance=pi)
            if form.is_valid():
                form.save()
        else:
            pi = Post.objects.get(pk=id)
            form = Postform(instance=pi)

    else:
         return HttpResponseRedirect('/login/')
    return render(request,'blog/updatepost.html',{'form':form})
  


# delete Post
def delete_post(request, id):
    if request.user.is_authenticated:
        pi = Post.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/dashboard/')
    else:
        return HttpResponseRedirect('/login/')




def user_profile(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = EditAdminProfile(request.POST,instance=request.user)
            if form.is_valid():
                messages.success(request,'Your Profile Has been Updated')
                form.save()
        else:
            form = EditAdminProfile(instance=request.user)   
        return render(request,'blog/userprofile.html',{'form':form})

    else:
        return HttpResponseRedirect('/login/')
        