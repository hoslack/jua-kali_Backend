from django.urls import path

from . import views

app_name = "products"

urlpatterns = [
    path('', views.ProductList.as_view(), name='all_products'),
    path('<int:pk>/', views.ProductDetail.as_view(), name='product_detail'),
]
