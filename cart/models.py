from django.db import models
from userAuthentication.models import Profile
from productsContent.models import Products


from django.conf import settings
from django.db.models.signals import post_save

class OrderItem(models.Model):

    product = models.OneToOneField(Products, on_delete=models.SET_NULL, null=True)
    is_ordered = models.BooleanField(default=False)
    quantity = models.IntegerField(default=1)

    def __str__(self) -> str:
        return self.product.model_name
    

    
class Order(models.Model):

    owner =  models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    items = models.ManyToManyField(OrderItem)
    ref_code = models.CharField(max_length=15)
    is_ordered = models.BooleanField(default=False)
    date_ordered = models.DateTimeField()

    def get_cart_items(self):
        return self.items.all()
    
    def get_cart_total(self):
        return sum( [item.product.price for item in self.items.all()] )
    
    def __str__(self) -> str:
        return f'{self.owner}, {self.ref_code}'
    



