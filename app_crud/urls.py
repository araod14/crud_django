from django.urls import path
from . import views


urlpatterns = [
    path('', views.index),
    path('new_task/', views.create_task, name='new_task'),
    path('delete_task/<int:task_id>/', views.delete_task ,          name='delete_task')
]
