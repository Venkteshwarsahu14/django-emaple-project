"""venkiscubetech URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from venkiscubetech import views

urlpatterns = [
    path("admin-panel/", admin.site.urls),
    path("", views.homePage),
    path("login/", views.login),
    path('about-us/', views.aboutUs),
    path("blogs/", views.blogs),
    path("submitform/", views.submitform, name="submitform"),
    path("register/", views.register),
    path("slug/", views.users),
    path("blogs/<blogid>", views.blogsDetails),
    path("userform/", views.userform),
    path("thanku/", views.thanku),
    path("calculator/", views.calculator),
    path("evenodd/", views.evenodd),
    path("marksheet/", views.marksheet),
    path("newsdetails/<newsid>", views.newsdeatils)
]
