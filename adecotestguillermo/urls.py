"""
URL configuration for adecotestguillermo project.

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
from guilletest.views import LoginView
from guilletest.views import home_view
from guilletest.views import logout_user
from guilletest.views import register
from guilletest.views import other_user_texts
from guilletest.views import scrape_view
from guilletest.views import scraping_history

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', LoginView.as_view(), name='login'),
    path('home/', home_view, name='home_view'),
    path('logout/', logout_user, name='logout'),
    path('registration/', register, name='register'),
    path('home-other-user/', other_user_texts, name='other_user_texts'),
    path('home-scraping/', scrape_view , name='scrape_view'),
    path('scraping-history/', scraping_history, name='scraping_history')
]
