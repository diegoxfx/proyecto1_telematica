"""DemeterTracker URL Configuration

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
from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView
from webapp import views as webapp_views
from api import views as api_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path('registration/', webapp_views.signup, name='signup'),
    path('events/list_events', webapp_views.list_events, name='list_events'),
    path('events/new_route', webapp_views.create_route, name='create_route'),
    path('events/list_routes', webapp_views.list_routes, name='route_list'),
    path('api/login', api_views.login),
    path('api/new_event', api_views.new_event),
    path('api/new_route', api_views.new_route),
    path('api/get_events', api_views.route_events)
]
