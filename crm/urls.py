
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    
    path('admin/', admin.site.urls),

    path('', include('webapp.urls')),

    path('', include('admin_material.urls')),
]
