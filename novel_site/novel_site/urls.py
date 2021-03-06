"""novel_site URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path, include
from login.views import login, register, logout
from book.views import user_space, about

urlpatterns = [
    path('books/', include('book.urls')),
    path('admin/', admin.site.urls),
    path('login/', login, name='login'),
    path('register/', register, name='register'),
    path('logout/', logout, name='logout'),
    path('user/<int:user_id>/', user_space, name='user_space'),   # 用户个人空间
    path('captcha/', include('captcha.urls')),   # 验证码
    path('about', about, name='about')
]
