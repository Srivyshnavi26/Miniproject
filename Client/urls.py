"""Analysis_of_Women_Safety URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from . import views

app_name="Client"
urlpatterns = [
              path('',views.user_login, name="user_login"),
              path("user_register",views.user_register, name="user_register"),
              path("user_mydetails",views.user_mydetails, name="user_mydetails"),
              path("user_updatedetails",views.user_updatedetails, name="user_updatedetails"),
              path("tweet",views.tweet, name="tweet"),
              path("tweetview",views.tweetview, name="tweetview"),
              path("feedback",views.feedback, name="feedback"),
]