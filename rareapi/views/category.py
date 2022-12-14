"""View module for handling requests about game types"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from rareapi.models import Post
from rareapi.models import Category


class CategoryView(ViewSet):
    """Categories view set"""

    def retrieve(self, request, pk):
        """Handle GET request for single category"""
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
    
    def create(self, request):
        """Handle GET operations"""
        category = Category.objects.create(
            label=request.data["label"]
        )
        serializer = CategoriesSerializer(category)
        return Response(serializer.data)
    
    def update(self, request, pk):
        """Handle PUT requests for a game"""
        category = Category.objects.get(pk=pk)
        category.label = request.data["label"]
        category.save()
        return Response(None, status=status.HTTP_204_NO_CONTENT)

    def destroy(self, request, pk):
        category = Category.objects.get(pk=pk)
        category.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)
class CategoriesSerializer(serializers.ModelSerializer):
    """serializer for categories"""
    class Meta:
        model = Category
        fields = ('id', 'label')
    
