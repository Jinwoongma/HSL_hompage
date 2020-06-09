from django.urls import path, include
from . import views

app_name = 'members'

urlpatterns = [
    path('', views.members_list, name='members_list'),
    path('create/', views.create_member, name='create_member'),
]  