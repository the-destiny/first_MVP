from django.contrib import admin
from django.urls import path, include
import home.views
import lectures.urls

urlpatterns = [
    path('admin/', admin.site.urls),
<<<<<<< HEAD
    path('', home.views.home, name="home"),
    path('lecture/', include('lectures.urls')), 
=======
    path('', home.views.home, name='home'),\
>>>>>>> dec9aa1... conflicts resolved
]
