from django.urls import path, include
from rest_framework import routers
from main_app import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


# Create routes for models
router = routers.SimpleRouter()
router.register(r'projects', views.ProjectViewSet, basename='projects')
router.register(r'bugs', views.BugViewSet, basename='bugs')
urlpatterns = [
    path('api/', include((router.urls, 'main_app'))),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
