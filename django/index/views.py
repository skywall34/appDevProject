from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
# Create your views here.
from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm
from django.db.models import Q
from django.contrib import messages
from django.contrib.auth import logout, authenticate, login, update_session_auth_hash
from django.http import HttpResponseRedirect
from django.core.mail import send_mail
from django.core.paginator import Paginator

from .forms import LoginForm, RegistrationForm, EditProfileForm,PostForm,TravelBlogForm
from .models import Post
from .filter import BlogFilter

import logging


@login_required
def Logout(request):
    logout(request)
    return HttpResponseRedirect('/')

class HomePageView(TemplateView):
    template_name = "index.html"



class TeamView(TemplateView):
    template_name = "team.html"

#Have this check if user is already logged in, also handle login method
#def register_user(request):
#    user_object = User()
    #check post request
#    if request.method == 'POST':
        #create a form instance and insert the data from the request
#        form = LoginForm(request.POST)

        #check valid
#        if form.is_valid():
#            user_object.username = form.cleaned_data['username']
#            user_object.password = form.cleaned_data['password']
#            user_object.email = form.cleaned_data['email']
#            user_object.first_name = form.cleaned_data['first_name']
#            user_object.last_name = form.cleaned_data['last_name']
#            user_object.save()
#            login(request, user_object)
#            return HttpResponseRedirect('/team/')
#
#    else:
#        form = LoginForm()
#
#    return render(request, 'login.html', {'form': form})


def register_user(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            send_mail('Subject Here',
                      'Here is the message',
                      'doshinkorean@gmail.com',
                      ['doshinkorean@utexas.edu'],
                      fail_silently=False, )
            return HttpResponseRedirect('/team/')
        else:
            print("request is not valid")
            print(form.errors)

    else:
        form = RegistrationForm()

        args = {'form': form}
        return render(request, 'register.html', args)



def login_user(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)

        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect('/team/')
        else:
            messages.error(request, 'username or password not correct')
            return redirect('/login/')

    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

@login_required
def profile(request):
    blog_filter = Post.objects.all().filter(username=request.user.username)  #
    args = {'user': request.user ,'blogs':blog_filter} #pass the entire object

    return render(request, 'profile.html', args)


def edit_profile(request):
    if request.method == "POST":
        form = EditProfileForm(request.POST, instance=request.user)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/profile/')

    else:
        form = EditProfileForm(instance=request.user)
        args =  {'form': form}
        return render(request, 'edit_profile.html', args)



def change_password(request):
    if request.method == "POST":
        form = PasswordChangeForm(data=request.POST, user=request.user)

        if form.is_valid():
            form.save()
            #keep the user logged in after change
            update_session_auth_hash(request, form.user)
            return HttpResponseRedirect('/profile/')

    else:
        form = PasswordChangeForm(user=request.user)
        args =  {'form': form}
        return render(request, 'change_password.html', args)


def send_email(request):
    send_mail('Subject Here',
              'Here is the message',
              'doshinkorean@gmail.com',
              ['doshinkorean@utexas.edu'],
              fail_silently=False,)
    return render(request, 'send_email.html')


@login_required
def create_post(request):
    #rint("create_post")
    #logging.debug("create_post")
    post_object = Post()
    if request.method == 'POST':
        #print("request is post")
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            #print("request is valid")
            #print(request.user)
            logging.debug(request.user)
            post_object.username = request.user
            post_object.title = form.cleaned_data['title']
            post_object.post_type = form.cleaned_data['post_type']
            post_object.country = form.cleaned_data['country']
            post_object.state = form.cleaned_data['state']
            post_object.city = form.cleaned_data['city']
            post_object.num_of_people = form.cleaned_data['num_of_people']
            post_object.theme = form.cleaned_data['theme']
            post_object.description = form.cleaned_data['description']
            post_object.image = form.cleaned_data['image']
            post_object.save()
            return HttpResponseRedirect('/profile/')
        else:
            print("request is not valid")
            print(form.errors)

    else:
        form = PostForm()
        args = {'form': form}
        return render(request, 'post.html', args)



def blogfilter(request):
    blog_list = Post.objects.all()
    blog_filter = BlogFilter(request.GET, queryset=blog_list)
    return render(request, 'travelblog.html', {'filter': blog_filter})



#def travelblog(request):
#    if request.method == 'GET':
#        query_country = request.GET.get('country')
#        query_state = request.GET.get('state')
#        query_theme = request.GET.get('theme')
#        results = Post.objects.filter(Q(country__icontains=query_country) & Q(state__icontains=query_state) & Q(theme__icontains=query_theme))

#        pages = Paginator(request, results, 2)
#        context = {
#            'blogs':pages[0],
#            'blog_range':pages[1],
#        }
#        return render(request, 'travelblog.html', context)



