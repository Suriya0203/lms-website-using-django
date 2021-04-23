"""product URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.conf.urls import include
from django.contrib import admin
from django.urls import path,include
from result.views import register_request,homepage,login_request,logout_request,home
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.core import checks


import debug_toolbar
urlpatterns = [
    path("", homepage, name="homepage"),
    path("register", register_request, name="register"),
    #path('', printl),
    path('home', home,name='home'),
    path('admin/', admin.site.urls),
    path("login", login_request, name="login"),
    path('debug/',include(debug_toolbar.urls)),
    #path('example_login/',auth_views.LoginView.as_view(template_name='example_login.html'),name='login)
    path("logout", logout_request, name= "logout")
]


from django.conf.urls.static import static
if settings.DEBUG:
    #import debug_toolbar

    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    #urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)