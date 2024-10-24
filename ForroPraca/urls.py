from django.contrib import admin
from django.urls import path, include
 # Certifique-se de que esta view exista

urlpatterns = [
    path('admin/', admin.site.urls),
    path('usuarios/', include('aplic.urls')),  