from django.db import models

class Product(models.Model):
    order_number = models.PositiveIntegerField(default=0, unique=True)
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image_url = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.name

class Order(models.Model):
    name = models.CharField(max_length=100)  # ชื่อ
    address = models.TextField()              # ที่อยู่
    phone = models.CharField(max_length=15)   # เบอร์โทร
    payment_method = models.CharField(max_length=50)  # ช่องทางการชำระเงิน

    def __str__(self):
        return f"Order {self.id} - {self.name}"