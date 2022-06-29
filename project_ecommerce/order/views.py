import stripe #to talk with the stripes api 

from django.conf import settings #to get the secret key 
from django.contrib.auth.models import User
from django.http import Http404 #if there are errors
from django.shortcuts import render 

from rest_framework import status, authentication, permissions
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Order, OrderItem
from .serializers import OrderSerializer, MyOrderSerializer

@api_view(['POST']) #post requests
@authentication_classes([authentication.TokenAuthentication]) #require token authentication 
@permission_classes([permissions.IsAuthenticated]) #user is authenticated 
def checkout(request):
    serializer = OrderSerializer(data=request.data) #data from the form that the user fill out in the checkout page

    if serializer.is_valid(): #if the data is correct, proceed with the checkout 
        stripe.api_key = settings.STRIPE_SECRET_KEY #initialize stripe with secret key from setting file
        paid_amount = sum(item.get('quantity') * item.get('product').price for item in serializer.validated_data['items']) #calculated the paid amount 

        try:                                 #if payment isn't successfull, accept this and show an error to the user
            charge = stripe.Charge.create(
                amount=int(paid_amount * 100), #multiply for 100 cus is need it in cents 
                currency='USD', #stablish the currency 
                description='Charge from PetStore', #bills
                source=serializer.validated_data['stripe_token'] #stripe token get it from the front end 
            )

            serializer.save(user=request.user, paid_amount=paid_amount) #save the data in the serializer,  
                                                                        #set the user to request the user, requested user and there is a paid amount 
            return Response(serializer.data, status=status.HTTP_201_CREATED) #to the front end knows everything is ok
        except Exception:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) #if something is going wrong with the serialiazer
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class OrdersList(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, format=None):
        orders = Order.objects.filter(user=request.user)
        serializer = MyOrderSerializer(orders, many=True)
        return Response(serializer.data)
