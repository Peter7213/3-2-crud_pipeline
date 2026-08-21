<<<<<<< HEAD
from rest_framework.routers import DefaultRouter

from .views import (ProductViewSet, StockViewSet)

router = DefaultRouter()
router.register('products', ProductViewSet)
router.register('stocks', StockViewSet)

urlpatterns = router.urls
=======
from rest_framework.routers import DefaultRouter

from .views import (ProductViewSet, StockViewSet)

router = DefaultRouter()
router.register('products', ProductViewSet)
router.register('stocks', StockViewSet)

urlpatterns = router.urls
>>>>>>> 30042147070ca8ae1b7d65d33bf2440b6229a2b8
