from django.contrib import admin
from django.urls import path

from tasks import views

urlpatterns = [
    path('', views.index, name='list'),
    path('update_task/<str:pk>', views.update_task, name='update_task'),
    path('delete_task/<str:pk>', views.DeleteTask, name='delete_task')
    ]