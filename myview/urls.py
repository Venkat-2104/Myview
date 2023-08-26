"""
URL configuration for myview project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from home.views import *
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('top_rated/',top_rated_page,name='top_rated'),
    path('logout/',logout_page,name='logout'),
    path('register/',register,name='register'),
    path('login/',login_page,name='login'),
    path('reviews/review/<id>/',reviews,name='reviews'),
    path('update_movie',update_movie,name='update_movie'),
    path('reviews/',re_front,name='reviews'),
    path('delete_movie/<id>/',delete_movie,name="delete_movie"),
    path('readdata/',  readdata , name = 'readdata'),
    path('home/',  home , name = 'home'),
    path('about/', about , name = 'about'),
    path('contact/', contact , name = 'contact'),
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

urlpatterns += staticfiles_urlpatterns()

