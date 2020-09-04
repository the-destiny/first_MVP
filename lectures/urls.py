from django.urls import path
from . import views

urlpatterns = [
    path('<slug:lecture_slug>/detail', views.detail, name="detail"),
    ]
     