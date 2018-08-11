from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
# Create your views here.
from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import logout, authenticate, login
from django.http import HttpResponseRedirect
from django.db import transaction
from django.urls import reverse
from django.contrib.auth.forms import UserCreationForm
from .forms import UserForm,ProfileForm,LoginForm, RegistrationForm


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
            return HttpResponseRedirect('/team/')

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
