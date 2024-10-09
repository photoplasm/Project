from django.shortcuts import render
from .models import Product

def index(request):
    products = Product.objects.all()  # ดึงผลิตภัณฑ์ทั้งหมด
    return render(request, 'index.html', {'products': products})
