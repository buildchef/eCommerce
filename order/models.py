from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Order(models.Model):
    user =  models.ForeignKey(User, on_delete=models.CASCADE)
    total = models.FloatField()
    status = models.CharField(
        default='C',
        max_length=1,
        choices=(
        ('A', 'Approved'),
        ('C', 'Created'),
        ('D', 'Disapproved'),
        ('P', 'Pending'),
        ('S', 'Sent'),
        ('F', 'Finished'),
    ))

    def __str__(self):
        return f'Order number {self.pk}'

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.CharField(max_length=255)
    product_id = models.PositiveIntegerField()
    variation = models.CharField(max_length=255)
    variation_id = models.PositiveIntegerField()
    price = models.FloatField()
    promotional_price = models.FloatField(default=0)
    quantity = models.PositiveIntegerField()
    image = models.CharField(max_length=2000)

    def __str__(self):
        return f'{self.order} item'
