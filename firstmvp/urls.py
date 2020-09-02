from django.contrib import admin
from django.urls import path
import home.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home.views.home, name = "home"), ##commit 전에 형식 확인하기
]
