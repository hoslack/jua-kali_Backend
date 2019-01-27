from rest_framework.exceptions import NotFound
from rest_framework.response import Response
from rest_framework import status
from .models import Category
from .serializers import CategorySerializer
from rest_framework import generics


class CategoryListCreate(generics.ListCreateAPIView):
    queryset = Category.objects.select_related()
    serializer_class = CategorySerializer


class CategoryCreateDeleteAPIView(generics.RetrieveUpdateDestroyAPIView,
                                  generics.CreateAPIView):
    """
    This view updates and deletes a category.
    It also creates a child to a category.
    """
    lookup_url_kwarg = 'pk'
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def destroy(self, request, pk=None):
        """Handle deleting a category."""
        try:
            pk = self.kwargs.get('pk')
        except Exception:
            raise NotFound('Please check your url, pk is missing')
        try:
            category = Category.objects.get(pk=pk)
        except Exception:
            raise NotFound('A category with this id does not exist.')
        category.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)

    def create(self, request, pk=None):
        """Create a child category on a parent category."""
        context = super(CategoryCreateDeleteAPIView,
                        self).get_serializer_context()
        try:
            # getting the parent category that will be the main category
            context['request'].data['parent'] = Category.objects.get(pk=pk).pk
        except Exception:
            raise NotFound('A category with this ID does not exist.')
        serializer = self.serializer_class(
            data=context['request'].data, context=context)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
