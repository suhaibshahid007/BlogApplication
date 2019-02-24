"""website URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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

from posts.views import *
from django.conf.urls import   re_path


urlpatterns = [
     re_path('create/$', posts_create),
     re_path('(?P<id>\d+)/edit/', posts_update),
     re_path('(?P<id>\d+)/delete/', posts_delete),
     re_path('(?P<id>\d+)', posts_detail),
     re_path( 'list/$', posts_list , name='list'),
]
