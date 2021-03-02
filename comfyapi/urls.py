from django.urls import path
from .views import ProductListView, ProductDetailView, ShippingProfileView
app_name = 'comfyapi'

urlpatterns = [
    path('products', ProductListView.as_view(), name='product-list'),
    path('products/<int:pk>', ProductDetailView.as_view(), name='product-detail'),
    path('shipping', ShippingProfileView.as_view(), name='shipping'),
]
