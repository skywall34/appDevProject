
from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.HomePageView.as_view(), name='home'), # HomePage
    url(r'^team/$', views.TeamView.as_view(), name='team'),
    url(r'^login/$', views.LoginView.as_view(), name='login'),
    url(r'^logout/$', views.Logout),

]