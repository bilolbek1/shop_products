from django.urls import path
from .views import ShopPageView, ProductPageView, AddProductView, EditProductView, EditShopView, \
    CategoryProductPageView, CategoryPageView, AddCategoryView, FilterProductView

urlpatterns = [
    path('', ShopPageView.as_view(), name='shop_page'),
    path('shop/<int:id>/edit', EditShopView.as_view(), name='edit-shop'),
    path('product/', ProductPageView.as_view(), name='product_page'),
    path('product/add/', AddProductView.as_view(), name='add-product'),
    path('product/<int:id>/edit', EditProductView.as_view(), name='edit-product'),
    path('product/price', FilterProductView.as_view(), name='product-filter'),
    path('product/<str:category_name>/', CategoryProductPageView.as_view(), name='category-product-page'),
    path('category/', CategoryPageView.as_view(), name='category-page'),
    path('category/add', AddCategoryView.as_view(), name='add-category'),
]
