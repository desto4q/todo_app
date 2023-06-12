from django.urls import path
from . import views

urlpatterns = [
    path("",views.task, name="home"),
    path("add/", views.addItem, name = "add"),
    path("get/<str:pk>", views.taskDetail, name = "get"),
    path("update/<str:pk>", views.Update, name = "update"),
    path("delete/<str:pk>", views.deletetask, name = "delete"),
]
