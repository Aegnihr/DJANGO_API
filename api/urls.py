from django.urls import path,include
from rest_framework import routers
from api import views

routers = routers.DefaultRouter()
routers.register('alumno', views.AlumnoViewSet)

urlpatterns = [
    path('', include(routers.urls))
]
