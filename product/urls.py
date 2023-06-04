from django.urls import path
from .views import ViewListProduct, ProductDetail, ViewCategory
from . import views
urlpatterns = [
    path('', ViewListProduct.as_view(), name='list-product'),
    path('detail/<int:pk>', ProductDetail.as_view(), name='detail-product'),
    path('category/<slug:category_slug>', ViewCategory.as_view(), name='category'),
    path('product_search/', views.search_product, name='product-search'),
]
