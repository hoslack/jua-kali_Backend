from django.urls import path

from . import views

app_name = "orders"

urlpatterns = [
    path('', views.OrderList.as_view(), name='all_orders'),
    path('<int:pk>/', views.OrderDetail.as_view(), name='order_detail'),
]
