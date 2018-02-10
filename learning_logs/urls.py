"""Defines url patterns for learning_logs."""

from django.conf.urls import url

from . import views

app_name = 'learning_logs'  #the weird code
urlpatterns = [
    # Home page.
    url(r'^$', views.index, name='index'),
    # TOPICS PAGE
    url(r'^topics/$', views.topics, name='topics'),
    # TOPIC DETAILS
    url(r'^topics/(?P<topic_id>\d+)/$', views.topic, name='topic')
]
