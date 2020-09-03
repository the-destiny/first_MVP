from django.contrib import admin
from django.urls import path, include
import lectures.urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('lecture/', include('lectures.urls')),
]
