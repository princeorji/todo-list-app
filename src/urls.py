from django.urls import path
from . import views

urlpatterns = [
    path('todo-list/', views.todoList, name="todo-list"),
    path('todo-detail/<str:pk>/', views.todoDetail, name="todo-detail"),
    path('create-todo/', views.createTodo, name="create-todo"),
    path('update-todo/<str:pk>/', views.updateTodo, name="update-todo"),
    path('delete-todo/<str:pk>/', views.deleteTodo, name="delete-todo"),
]
