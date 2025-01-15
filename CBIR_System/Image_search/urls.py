"""
URL configuration for CBIR_System project.

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
from Image_search import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
   path("" , views.index , name="ImageSearch"),  #If blank path then run index function
   path("index.html" , views.index , name="ImageSearch"), 
   path("Search.html" , views.Search , name="ImageSearch"),
   path("add_data/" , views.add_person , name="add_data")
   
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
