from django.contrib import admin
from django.conf.urls import include, url
from django.contrib.auth import views
from django.contrib.auth.views import LogoutView
from django.contrib.auth.views import LoginView

urlpatterns = [
    url('admin/', admin.site.urls),
    url(r'^accounts/login/$', views.LoginView.as_view(), name='login'),
    url(r'^accounts/logout/$', views.LogoutView.as_view(), name='logout', kwargs={'next_page': '/'}),
    url(r'', include('citas.urls')),
]
