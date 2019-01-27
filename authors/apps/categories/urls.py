"""Define the urls of the comment app."""
from django.urls import path

from . import views

app_name = "categories"

urlpatterns = [
    path('', views.CategoryListCreate.as_view(), name='all_categories'),
    path('<int:pk>/', views.CategoryCreateDeleteAPIView.as_view(), name='category_detail'),
]
