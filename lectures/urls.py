from django.urls import path
from . import views

urlpatterns = [
    path('detail/<slug:lecture_slug>/', views.detail, name='detail'),
    path('detail/<slug:lecture_slug>/<int:lecture_id>/', views.playlist_first, name='playlist_first'),
    path('detail/<slug:lecture_slug>/<int:lecture_id>/clicked/', views.playlist_clicked, name='playlist_clicked'),
]
