from django.contrib import admin
from django.urls import path
from aplic import views  # importe sua view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home),
]
