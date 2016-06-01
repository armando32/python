from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^account/$', views.AccountList, name='account_list'),
    url(r'^session/$', views.SessionList, name='session_list'),
    url(r'^message/$', views.MessageList, name='message_list'),
    url(r'^verification/$', views.VerificationList, name='verification_list'),       
]