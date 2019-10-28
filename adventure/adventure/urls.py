"""adventure URL Configuration

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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin

from django.urls import path, include
from trail.views import HomeView, UserCreateView, AddTrailView, SearchTrailView, TrailView, ContactView, UsersView
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomeView.as_view(), name='home'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('user_create/', UserCreateView.as_view()),
    path('add_trail/', AddTrailView.as_view()),
    path('search_trail/', SearchTrailView.as_view(), name='search-trail'),
    path('trail_view/<int:pk>/', TrailView.as_view(), name='trail-view'),
    path('contact/', ContactView.as_view(), name='contact'),
    path('users/', UsersView.as_view()),
    ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

