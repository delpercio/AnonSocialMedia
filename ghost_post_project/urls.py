"""ghost_post_project URL Configuration

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
from django.contrib import admin
from django.urls import path
from ghost_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('boasts/', views.boasts_view),
    path('roasts/', views.roasts_view),
    path('submit/', views.submit_view),
    path('sorted/', views.sorted_view),
    path('',views.index_view)
]
# TODO
# NEED TO LINK ALL URLS TO PAGES
# NEED TO ADD BUTTONS TO GO TO BOASTS OR ROASTS
# NEED TO HAVE A VIEW THAT WILL SORT BY SCORE (UP - DOWN VOTES)