"""Tales URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from authentication.views import Login_view, Signup_view, logout_view
from home.views import index_view, user_detail
from stories.views import Create_Book, upload_chapter

urlpatterns = [
    path('chapter/<int:book_id/', upload_chapter),
    path('profile/<int:user_id>/', user_detail),
    path('createbook/', Create_Book),
    path('', index_view, name='home'),
    path('signup/', Signup_view),
    path('logout/', logout_view),
    path('login/', Login_view),
    path('admin/', admin.site.urls),
]
