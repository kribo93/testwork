"""studentbase URL Configuration

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
from testbase.views import GroupListView,GroupDetailView, MyLoginView, GroupCreateView,StudentCreateView, StudentUpdateView, GroupUpdateView,GroupDeleteView, StudentDeleteView

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^login/$', MyLoginView.as_view(), name='login'),
    url(r'^admin/', admin.site.urls),
    url(r'^$', GroupListView.as_view(), name='home'),
    url(r'^group/(?P<pk>\d+)/detail/$', GroupDetailView.as_view(), name='group_detail'),
    url(r'^group_create/$', GroupCreateView.as_view(), name='group_create'),
    url(r'^group/(?P<pk>[\w-]+)/edit$', GroupUpdateView.as_view(), name='group_edit'),
    url(r'^group/(?P<pk>[\w-]+)/delete$', GroupDeleteView.as_view(), name='group_delete'),

    url(r'^student_create/$', StudentCreateView.as_view(), name='student_create'),
    url(r'^student/(?P<pk>[\w-]+)/edit$', StudentUpdateView.as_view(), name='student_edit'),
    url(r'^student/(?P<pk>[\w-]+)/delete$', StudentDeleteView.as_view(), name='student_delete'),
]

if settings.DEBUG:
    urlpatterns += static(settings. MEDIA_URL, document_root=settings.MEDIA_ROOT)