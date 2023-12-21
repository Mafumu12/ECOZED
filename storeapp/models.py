from django.db import models
from django.contrib.auth.models import User
import uuid

class Category(models.Model):
    name = models.CharField(max_length = 200)
    def __str__(self) :
        return self.name

class Seller(models.Model):
    name = models.OneToOneField(User,on_delete=models.CASCADE)
    def __str__(self) :
        return self.name
class Product(models.Model):
    Name = models.CharField(max_length=200)
    Description = models.TextField()
    Price = models.DecimalField(max_digits=7,decimal_places=2)
    Image = models.ImageField(upload_to='images/')
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    seller = models.ForeignKey(User,on_delete=models.CASCADE)
    Created = models.DateTimeField(auto_now_add=True)
    def __str__(self) :
        return self.Name

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    email = models.EmailField()

    def __str__(self):
        return self.user.username
    
class Cart(models.Model):
    customer = models.ForeignKey(Customer,on_delete=models.CASCADE)
    cart_id = models.UUIDField(default=uuid.uuid4,unique=True, editable=False)
    completed = models.BooleanField(default=False)
    
    @property
    def get_cart_total(self):
        cartitems = self.cartitems_set.all()
        total = sum([item.get_total for item in cartitems])
        return total
    
    @property
    def items_total(self):
        cartitems = self.cartitems_set.all()
        total = sum([item.quantity for item in cartitems])
        return total
    
    def __str__(self):
     return str(self.cart_id)


class Cartitems(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)

     
    

    @property
    def get_total(self):
        total = self.quantity * self.product.Price
        if total == 0.00:
            self.delete()
        return total
    

    
    
    def __str__(self):
     return f"Cartitem - {self.cart.cart_id} - {self.product.Name}"




class Shipping_Info(models.Model):
    Customer = models.ForeignKey(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    email = models.EmailField( )
    Cart = models.ForeignKey(Cart,on_delete=models.CASCADE)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    state = models.CharField(max_length=200)
    zipcode = models.IntegerField()
    def __str__(self) :
        return self.address



