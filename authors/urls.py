"""authors URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include
from django.contrib import admin
from django.urls import path

from django.conf.urls import url
from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title="Author's Haven")

schema_view.view_initkwargs['permission_classes'].clear()

urlpatterns = [
    url(r'^$', schema_view),
    path('admin/', admin.site.urls),
    path('api/v1/articles/',
         include('authors.apps.articles.urls', namespace='articles')),
    path('api/v1/products/',
         include('authors.apps.products.urls', namespace='products')),
    path('api/v1/orders/',
         include('authors.apps.orders.urls', namespace='orders')),
    path('api/v1/articles/<str:slug>/comments/',
         include('authors.apps.comments.urls', namespace='comments')),
    path(
        'api/v1/',
        include(
            'authors.apps.authentication.urls', namespace='authentication')),
    path('api/v1/profiles/',
         include('authors.apps.profiles.urls', namespace='profiles')),
]