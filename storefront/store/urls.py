from django.urls import include
from django.urls import path
from rest_framework.routers import SimpleRouter
from . import views

router = SimpleRouter()                                                     # use Routers to get prodcus and collection end point
router.register('products',views.ProductViewSet)
router.register('collections',views.CollectionViewSet)

# URLConf

urlpatterns = [
    path('',include(router.urls))
    # path('products/', views.ProductList.as_view()),
    # path('products/<int:pk>', views.Prodcutdetail.as_view()),
    # path('collections/', views.CollectionList.as_view()),
    # path('collections/<int:pk>', views.CollectionDetail.as_view(),name= 'collection-detail')          # Mind ! the pk here instead id 

]
