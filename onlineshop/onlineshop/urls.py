"""onlineshop URL Configuration

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
from django.urls import path
from django.shortcuts import HttpResponse
from django.shortcuts import render
from dashboard.views import produk
from dashboard.views import tambah_barang
from dashboard.views import Barang_View, Member 

def coba(request):
    return HttpResponse('hallo')

def satu(request):
    titelnya="Home"
    konteks = {
        'titel':titelnya,
    }
    return render(request, 'home.html',konteks)

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', coba),
    path('',satu, name='home'),
    path('produk/',produk, name='produk'),
    path('addbrg/',tambah_barang),
    path('vbrg/',Barang_View, name='barang'),
    path('member/', Member, name='member'),
    

]
