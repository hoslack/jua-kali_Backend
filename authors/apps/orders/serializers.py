from rest_framework.exceptions import PermissionDenied, NotFound
from rest_framework import serializers

from .models import Order
from ..authentication.serializers import UserSerializer
from ..products.serializers import ProductSerializer
from ..products.models import Product


class OrderSerializer(serializers.ModelSerializer):

    owner = UserSerializer(read_only=True)
    product = ProductSerializer(read_only=True)

    class Meta:
        model = Order
        fields = '__all__'
        lookup_url_kwarg = 'id'

    def create(self, validated_data):
        """Handle creating a new comment."""
        product_id = self.context['request'].data.get('product')
        try:
            product = Product.objects.get(pk=product_id)
        except Product.DoesNotExist:
            raise NotFound('Product does not exist, You cannot make an order')
        try:
            owner = self.context['request'].user
        except self.context['request'].user.DoesNotExist:
            raise PermissionDenied(
                'Please log in first to perform this action')
        order = Order.objects.create(
            owner=owner, product=product, **validated_data)
        return order
