from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_routes),
    path('tasks/', views.get_tasks),
    path('tasks/create/', views.create_task),
    path('task/<str:pk>', views.update_task),
    path('task/delete/<str:pk>', views.remove_task)
]