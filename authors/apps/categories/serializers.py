from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from .models import Category


class RecursiveField(serializers.Serializer):
    def to_representation(self, value):
        serializer = self.parent.parent.__class__(value, context=self.context)
        return serializer.data


class CategorySerializer(serializers.ModelSerializer):
    name = serializers.CharField(required=True, max_length=255,
                                 validators=[UniqueValidator(queryset=Category.objects.all())])
    children = serializers.ListSerializer(read_only=True, child=RecursiveField())

    class Meta:
        model = Category
        fields = '__all__'
        lookup_url_kwarg = 'pk'

    def create(self, validated_data):
        category = Category.objects.create(
            **validated_data
        )
        return category
