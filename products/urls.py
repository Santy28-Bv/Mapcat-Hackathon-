# products/urls.py
from rest_framework.routers import DefaultRouter
#from .views import ProductViewSet
from .api import ProductViewSet
from .api import CategoryViewSet
from .api import SubCategoryViewSet

router = DefaultRouter()
router.register('products', ProductViewSet, basename='products')
router.register('categories', CategoryViewSet, basename='categories')
router.register('subcategories', SubCategoryViewSet, basename='subcategories')

urlpatterns = router.urls

