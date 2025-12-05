# products/urls.py
from rest_framework.routers import DefaultRouter
from .api import ProductViewSet
from .api import CategoryViewSet
from .api import SubCategoryViewSet
from .api import UserViewSet   # 👈 nuevo import

router = DefaultRouter()
router.register('products', ProductViewSet, basename='products')
router.register('categories', CategoryViewSet, basename='categories')
router.register('subcategories', SubCategoryViewSet, basename='subcategories')
router.register('users', UserViewSet, basename='users')  # 👈 nuevo endpoint

urlpatterns = router.urls