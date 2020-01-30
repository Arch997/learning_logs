# -*- coding: utf-8 -*-

"""Defines URL patterns for learning_logs"""

from django.urls import path, re_path
from . import views

urlpatterns = [
	# Home page
	re_path(r'^$', views.index, name='index'),
	path("topics/", views.topics, name='topics'),
	
	# Matches the integer and stores the value in 'topic_id'
	path("topics/<int:topic_id>/", views.topic, name='topic'),
	#re_path(r'^topics/(?P<topic_id>\d+)/$', views.topic, name='topic'),
	path("new_topic/", views.new_topic, name="new_topic"),
	#Mew entries
	path("new_entry/<int:topic_id>/", views.new_entry, name='new_entry'),
	#Edit entry
	path("edit_entry/<int:entry_id>/", views.edit_entry, name='edit_entry'),
	]
