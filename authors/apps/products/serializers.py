from rest_framework import serializers

from .models import Product
from ..authentication.serializers import UserSerializer


class ProductSerializer(serializers.ModelSerializer):
    name = serializers.CharField(
        required=True,
        max_length=255,
    )
    producer = UserSerializer(read_only=True)

    class Meta:
        model = Product
        fields = '__all__'
        lookup_url_kwarg = 'id'

    def create(self, validated_data):
        producer = self.context['request'].user
        product = Product.objects.create(
            producer=producer,
            **validated_data
        )
        return product
