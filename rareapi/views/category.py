"""View module for handling requests about game types"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from rareapi.models import Post
from rareapi.models import Category


class CategoryViewSet(ViewSet):
    """Categories view set"""

    def retrieve(self, request, pk):
        """Handle GET request for single post
        Returns:
            Response JSON serielized post instance
        """
        try:
            category = Category.objects.get(pk=pk)
            serializer = CategoriesSerializer(category, context={'request': request})
            return Response(serializer.data)
        except Exception as ex:
            return HttpResponseServerError(ex)


    def list(self, request):
        """GET all categories"""
        categories = Category.objects.all()

        serialized_categories = CategoriesSerializer(categories, many=True)
        return Response(serialized_categories.data, status=status.HTTP_200_OK)
    
    def destroy(self, pk):
        category = Category.objects.get(pk=pk)
        category.delete()
        return Response({}, status=status.HTTP_204_NO_CONTENT) 
      
class CategoriesSerializer(serializers.ModelSerializer):
    """serializer for categories"""
    class Meta:
        model = Category
        fields = ('id', 'label')
    
