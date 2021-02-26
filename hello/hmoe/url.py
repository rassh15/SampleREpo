# -*- coding: utf-8 -*-
"""
Created on Mon Feb 22 16:12:23 2021

@author: rassh
"""

from django.contrib import admin
from django.urls import path
from hmoe import views


urlpatterns = [

        path('', views.index, name='HOME'),
        path("about/", views.about, name='ABOUT'),
        path("service/", views.service, name='SERVICES'),
        
        path("contact/", views.contact, name='CONTACT')
]
     