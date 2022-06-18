from django.contrib.auth.models import User #user object requests authenticated 
from django.db import models
from product.models import Product #item is conected to product

class Order(models.Model):
    user = models.ForeignKey(User, related_name='orders', on_delete=models.CASCADE) #conect the user to the order
    first_name = models.CharField(max_length=100) #contac information 
    last_name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    zipcode = models.CharField(max_length=100)
    place = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True) #to know when the order was made it 
    paid_amount = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True) #get from stripe
    stripe_token = models.CharField(max_length=100) #to perform the purchase 

    class Meta:
        ordering = ['-created_at',] #changed the ordering to create it at in descending order, so in the backend everything is okay, 
                                    #and when you show the ordering and then my account page
    def __str__(self):
        return self.first_name #string representation, easier to see in the back end 

class OrderItem(models.Model): #order item, 
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE) #reference to the order
    product = models.ForeignKey(Product, related_name='items', on_delete=models.CASCADE) #reference to the product
    price = models.DecimalField(max_digits=8, decimal_places=2) 
    quantity = models.IntegerField(default=1) 

    def __str__(self):
        return '%s' % self.id #to see in the back end 


