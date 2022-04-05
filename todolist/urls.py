from django.urls import path
from . import views

urlpatterns = [
        path('',views.login,name='main'),
        path('create',views.create,name='create'),
        path('login',views.login,name='login'),
        path('todolist',views.todolist,name='todolist'),
        path('todolist/<main>', views.action, name='detail'),
        ]
