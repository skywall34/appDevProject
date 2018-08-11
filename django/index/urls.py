
from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.HomePageView.as_view(), name='home'), # HomePage
    url(r'^team/$', views.TeamView.as_view(), name='team'),
    url(r'^login/$', views.login_user, name='login'), # register first for newcomers
    url(r'^logout/$', views.Logout),
    url(r'^register/$', views.register_user, name='register'),

]
