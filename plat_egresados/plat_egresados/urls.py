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
    url(r'^profile_graduated/(?P<id_user>\d+)$', views.profile_graduated, name='profile_graduated'),
    url(r'^profile_admin$', views.profile_admin, name='profile_admin'),
    url(r'^activate_graduated$', views.active_graduated, name='active_graduated'),
    url(r'^activate_admin$', views.active_admin, name='active_admin'),
    url(r'^activate_user/(?P<id_user>\d+)$', views.activate_user, name='activate_user'),
    url(r'^delete_user/(?P<id_user>\d+)$', views.delete_user, name='delete_user'),
    url(r'^list_graduated$', views.list_graduated, name='list_graduated'),
    url(r'^list_admin$', views.list_admin, name='list_admin'),
    url(r'^create_notice$', views.create_notice, name='create_notice'),
    url(r'^create_category$', views.create_category, name='create_category'),
    url(r'^desactivate_user/(?P<id_user>\d+)$', views.desactivate_user, name='desactivate_user'),
    url(r'^delete_category/(?P<category>\d+)$', views.delete_category, name='delete_category'),
    url(r'^edit_admin/(?P<id_user>\d+)$', views.edit_admin, name='edit_admin'),
    url(r'^edit_graduated/(?P<id_user>\d+)$', views.edit_graduated, name='edit_graduated'),
    url(r'^edit_category/(?P<category>\d+)$', views.edit_category, name='edit_category'),
    url(r'^delete_notice/(?P<id_notice>\d+)$', views.delete_notice, name='delete_notice'),
    url(r'^edit_notice/(?P<id_notice>\d+)$', views.edit_notice, name='edit_notice'),
    url(r'^interests$', views.interests, name='interests'),
    url(r'^add_interests/(?P<category>\d+)$', views.add_interests, name='add_interests'),
    url(r'^delete_interests/(?P<category>\d+)$', views.delete_interests, name='delete_interests'),
    url(r'^friends$', views.friends, name='friends'),
    url(r'^add_friends/(?P<friend>\d+)$', views.add_friends, name='add_friends'),
    url(r'^delete_friends/(?P<friend>\d+)$', views.delete_friends, name='delete_friends'),
    url(r'^send_message/(?P<friend>\d+)$', views.send_message, name='send_message'),
    url(r'^change_password$', views.change_password, name='change_password'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
