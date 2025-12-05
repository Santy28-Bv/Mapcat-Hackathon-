# user/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .api import UserViewSet   # ✅ importa el viewset correcto

router = DefaultRouter()
router.register(r'users', UserViewSet, basename='user')
urlpatterns = router.urls
