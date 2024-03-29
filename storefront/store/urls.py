from django.urls import include
from django.urls import path
from rest_framework.routers import SimpleRouter
from rest_framework_nested import routers
from . import views

router = routers.DefaultRouter()                                                   # use Routers to get prodcus and collection end point
router.register('products',views.ProductViewSet)
router.register('collections',views.CollectionViewSet)
router.register('carts',views.CartViewSet)
# router.register('carts',views.CartViewSet)
products_router = routers.NestedDefaultRouter(router,'products',lookup = 'product')
products_router.register('reviews',views.ReivewViewSet,basename='product-reviews')

Cart_router = routers.NestedDefaultRouter(router,'carts',lookup = 'cart')
Cart_router.register('items',views.ItemViewSet,basename = 'cart-items')



# URLConf

urlpatterns = [
    path('',include(router.urls)),
    path('',include(products_router.urls)),
    path('',include(Cart_router.urls))
    # path('products/', views.ProductList.as_view()),
    # path('products/<int:pk>', views.Prodcutdetail.as_view()),
    # path('collections/', views.CollectionList.as_view()),
    # path('collections/<int:pk>', views.CollectionDetail.as_view(),name= 'collection-detail')          # Mind ! the pk here instead id 

]
