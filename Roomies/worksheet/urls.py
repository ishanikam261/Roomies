from django.urls import path
from . import views

urlpatterns = [
    path('', views.task_list, name='task_list'),
    path('create/', views.create_task, name='create_task'),
    path('update/<int:pk>/', views.update_task, name='update_task'),
    path('delete/<int:pk>/', views.delete_task, name='delete_task'),
    path("login/", views.adminLoginView.as_view(), name="admin_login"),
     path('edit/', views.edit, name='edit'),
      path('complete/<int:pk>/', views.complete_task, name='complete'),
]
