"""Analysis_of_Women_Safety path Configuration

The `pathpatterns` list routes paths to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/paths/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a path to pathpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a path to pathpatterns:  path('', Home.as_view(), name='home')
Including another pathconf
    1. Import the include() function: from django.paths import include, path
    2. Add a path to pathpatterns:  path('blog/', include('blog.paths'))
"""
from django.urls import path,include
from . import views

app_name="Research"
urlpatterns = [
      path('admin_login', views.admin_login, name="admin_login"),
      path('viewspage', views.admin_viewpage, name="admin_viewpage"),
      path('viewsfeedback', views.admin_viewfeedback, name="admin_viewfeedback"),
      path('viewstrending', views.admin_viewtrending, name="admin_viewtrending"),
      path('viewtreandingtopics/(?P<chart_type>\w+)/$', views.viewtreandingtopics,
          name="viewtreandingtopics"),
      path('negativefeedbacktivechart/(?P<chart_type>\w+)/$', views.negativefeedbacktivechart,
          name="negativefeedbacktivechart"),
]