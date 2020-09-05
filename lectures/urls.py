from django.urls import path
from . import views

urlpatterns = [
    path('<slug:lecture_slug>/detail/', views.detail, name='detail'),
    path('listup/', views.listup, name='listup'),
    path('listup_categ/', views.listup_categ, name='listup_categ'),
]
