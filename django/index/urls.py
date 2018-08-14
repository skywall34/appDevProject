
from django.conf.urls import url, include
from django.contrib.auth import views as auth_views
from . import views



urlpatterns = [
    url(r'^$', views.HomePageView.as_view(), name='home'), # HomePage
    url(r'^team/$', views.TeamView.as_view(), name='team'),
    url(r'^login/$', views.login_user, name='login'), # register first for newcomers
    url(r'^logout/$', views.Logout),
    url(r'^register/$', views.register_user, name='register'),
    url(r'^profile/$', views.profile, name='profile'),
    url(r'^profile/edit/$', views.edit_profile, name='edit_profile'),
    url(r'^change-password/$', views.change_password, name='change_password'),
    url('^', include('django.contrib.auth.urls')),
    url('^reset-password/$', auth_views.PasswordResetView.as_view(template_name="password_reset.html")),
    url('^reset-password/done$', auth_views.PasswordResetDoneView.as_view(template_name="password_reset.html")),
    url('^reset-password/confirm/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$', auth_views.PasswordResetConfirmView.as_view(template_name="password_reset.html")),
    url('^reset-password/complete/$', auth_views.PasswordResetCompleteView.as_view(template_name="password_reset.html")),
    url('^send-email/$', views.send_email, name='send_email'),
    url('^create-post/$', views.create_post, name='create_post')
]
