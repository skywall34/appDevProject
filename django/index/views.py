from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
# Create your views here.
from django.conf import settings
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm
from django.contrib import messages
from django.contrib.auth import logout, authenticate, login, update_session_auth_hash
from django.http import HttpResponseRedirect
from django.core.mail import send_mail
from django.core.paginator import Paginator

#for the android REST API
from django.contrib.auth.models import User, Group
from rest_framework import viewsets, status
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import UserSerializer, GroupSerializer, BlogSerializer

from .forms import LoginForm, RegistrationForm, EditProfileForm,PostForm,TravelBlogForm
from .models import Post
from .filter import BlogFilter

#for the Google Maps API
from geopy.geocoders import Nominatim



import logging


@login_required
def Logout(request):
    logout(request)
    return HttpResponseRedirect('/')

class HomePageView(TemplateView):
    template_name = "index.html"




class TeamView(TemplateView):
    template_name = "team.html"


# This takes a while before the email makes it
def register_user(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data['email']
            str(email)
            send_mail('Register Confirmation',
                      'Thank you for registering with TOGETHER! You can now create and edit blogs!',
                      '',
                      [email],
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



def password(request):
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
        return render(request, 'password.html', args)


def send_email(request):
    send_mail('Subscription Update',
              'Thank you for subscibing to TOGETHER! For now we are a new service so we will send updates when we can!',
              'together@gmail.com',
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
        #print(form)
        theme = request.POST['theme']
        post_type = request.POST['post_type']
        print(theme)
        #get input of theme
        if form.is_valid():
            #print("request is valid")
            #print(request.user)
            logging.debug(request.user)
            post_object.username = request.user
            post_object.title = form.cleaned_data['title']
            post_object.post_type = post_type
            post_object.country = form.cleaned_data['country']
            post_object.state = form.cleaned_data['state']
            post_object.city = form.cleaned_data['city']
            post_object.num_of_people = form.cleaned_data['num_of_people']
            post_object.theme = theme
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
    #country is given
    autofill_list_state = []
    autofill_list_theme = []
    for i in range(len(blog_list)):
        autofill_list_state.append(blog_list[i].state)
        autofill_list_theme.append(blog_list[i].theme)
    blog_filter = BlogFilter(request.GET, queryset=blog_list)
    return render(request, 'travelblog.html', {'filter': blog_filter, 'autofill_list_state': autofill_list_state, 'autofill_list_theme': autofill_list_theme})


def blog_summary(request, pk):
    single_blog = Post.objects.get(pk=pk)
    geolocator = Nominatim(user_agent="django")
    location = geolocator.geocode(single_blog.city, timeout=10)
    #print(location.address)
    #print((location.latitude, location.longitude))
    return render(request, 'blog_summary.html', {'single_blog': single_blog, 'lat':location.latitude, 'long': location.longitude})


def theme_list(request, item):
    blog_list_filter = Post.objects.filter(post_type=item)  # filter by theme
    return render(request, 'theme_list.html', {'filter': blog_list_filter})


#for the android REST API
#http://www.django-rest-framework.org/
class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class BlogViewSet(viewsets.ModelViewSet):
    #API endpoint for all posts
    queryset = Post.objects.all()
    serializer_class = BlogSerializer










