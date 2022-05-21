"""doubleclick URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home),
    path('home/', views.home),
    path('engine/',views.engine),
    path('vehicle/',views.vehicle),
    path('brake/',views.brake),
    path('ac/',views.ac),
    path('price/',views.price),
    path('wait/',views.wait),
    path('cont/',views.cont),
    path('history/',views.history),
    path('team/',views.team),
    path('news/',views.news),
    path('promo/',views.promo),
    path('launch/',views.launch),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
