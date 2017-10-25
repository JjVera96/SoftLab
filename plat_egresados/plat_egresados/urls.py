"""plat_egresados URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from app import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^login$', views.view_login, name='login'),
    url(r'^first_entrance/(?P<id_user>\d+)$', views.first_entrance, name='first_entrance'),
    url(r'^logout$', views.view_logout, name='logout'),
    url(r'^no_registred$', views.no_registred, name='no_registred'),
    url(r'^register$', views.register, name='register'),
    url(r'^forget_account$', views.forget_account, name='forget_account'),
    url(r'^register_graduated$', views.register_graduated, name='register_graduated'),
    url(r'^register_admin$', views.register_admin, name='register_admin'),
    url(r'^$', views.index, name='index'),
    url(r'^profile_graduated$', views.index_graduated, name='index_graduated'),
    url(r'^profile_admin$', views.index_admin, name='index_admin'),
    url(r'^profile_root$', views.index_root, name='index_root'),
    url(r'^activate_graduated$', views.active_graduated, name='active_graduated'),
    url(r'^activate_admin$', views.active_admin, name='active_admin'),
    url(r'^activate_user/(?P<id_user>\d+)$', views.activate_user, name='activate_user'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
