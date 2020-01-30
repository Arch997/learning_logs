# -*- coding: utf-8 -*-

from django.urls import path
from django.contrib.auth.views import LoginView

from . import views

"""Login page: Send requests to Django's default login view not users app views.py. Because we’re not writing our own view  function, wepass a dictionary telling Django where to find the template we’re about to write. This template will be part of the users app, not the learning_logs app."""

urlpatterns = [
	# Login page
	path('login/', LoginView.as_view(template_name = 'users/login.html'),
	  name='login'),
	path('logout/', views.logout_view, name='logout'),
	# Registration page
	path('register/', views.register, name='register'),
	]
