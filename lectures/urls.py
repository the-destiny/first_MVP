from django.urls import path
from . import views

urlpatterns = [
    path('<slug:lecture_slug>/detail/', views.detail, name='detail'),
    path('listup/', views.listup, name='listup'),
    path('listup_categ/', views.listup_categ, name='listup_categ'),
    path('detail/<slug:lecture_slug>/<int:lecture_id>/', views.playlist_first, name='playlist_first'),
    path('detail/<slug:lecture_slug>/<int:lecture_id>/clicked/', views.playlist_clicked, name='playlist_clicked'),
]
