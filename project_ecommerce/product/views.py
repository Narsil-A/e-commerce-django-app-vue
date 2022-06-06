from django.db.models import Q 
from django.http import Http404

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view #search funcionality

from .models import Product, Category
from .serializers import ProductSerializer, CategorySerializer


class LatestProductsList(APIView):
    def get(self, request, format=None):
        products = Product.objects.all()[0:4] #get products from the db, the firts 4 numbers [0:4]
        serializer = ProductSerializer(products, many= True) #convert to json, many=True bcz we have more than one object. 
        return Response(serializer.data)
    
class ProductDetail(APIView):
    def get_object(self, category_slug, product_slug): #check if the product exists 
        try:
            return Product.objects.filter(category__slug=category_slug).get(slug=product_slug) #we filter every product that is inside
        except Product.DoesNotExist:                                                           #get the slug of the products if exist, and 
            raise Http404        #raise 404 error, from django.http                            #if it doesnt exist we will get and exeption
        
    def get(self, request, category_slug, product_slug, format=None): #get the product function
        product = self.get_object(category_slug, product_slug)
        serializer = ProductSerializer(product)
        return Response(serializer.data)    #passing the serializer 
    
class CategoryDetail(APIView):
    def get_object(self, category_slug):
        try:
            return Category.objects.get(slug=category_slug)
        except Product.DoesNotExist:
            raise Http404

    def get(self, request, category_slug, format=None):
        category = self.get_object(category_slug)
        serializer = CategorySerializer(category)
        return Response(serializer.data)   
    
    
    
@api_view(['POST']) #decorator to accept post request to this view
def search(request): #search query 
    query = request.data.get('query', '') #get the query from request data, if its empty, is empty. 
    
    if query:
        products = Product.objects.filter(Q(name__icontains=query) | Q(description__icontains=query)) #check if the name contains the query
        serializer = ProductSerializer(products, many=True)                                           #or description 
        return Response(serializer.data)      #return data json                                       #import Q function of djando, allows to make advanced query sets
    else: 
        return Response({"products":[]}) #if the query is empty, return a empty product list 