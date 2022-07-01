from django.urls import path, include
from rest_framework import routers
from main_app import views

# Create routes for models
router = routers.SimpleRouter()
router.register(r'projects', views.ProjectViewSet, basename='projects')
urlpatterns = [
    path('/api/', include((router.urls, 'main_app'))),
]