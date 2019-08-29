"""project2 URL Configuration

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
from django.conf import settings
from django.contrib import admin
from django.conf.urls import url
from app2 import views
from django.views.static import serve

urlpatterns = [
    url('admin/', admin.site.urls),
    url(r'^$', views.login_view),
    url(r'^newuser/', views.registration_view),
    url(r'^login/', views.login_view),
    url(r'^home',views.upload_fetch_view),
    url(r'^showimage',views.images),
    url(r'^showdata',views.table_view),
    url(r'^images/', views.feedback_view),
    url(r'^contact/', views.contact_view),
    url(r'^about/', views.about_view),
    url(r'^feedback/',views.feedback_view),
    url(r'^update/<int:pid>/',views.update_view),
    url(r'edit/<int:pid>/', views.edit),
    url(r'^delete/',views.delete_view),
]

if settings.DEBUG:
    urlpatterns+=[url(r'^media/(?P<path>.*)$', serve, {
        'document_root': settings.MEDIA_ROOT})]