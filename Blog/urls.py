from django.urls import path
from . import views


urlpatterns = [
    path('',views.index,name='home'),
    path('post/<pk>', views.content,name='content'),
    path('projects', views.projects,name='projects'),
    path('teams/',views.teams, name='teams'),
    path('posts/',views.AllPost,name='blog'),
    path('contact/',views.contact,name='contact')
]